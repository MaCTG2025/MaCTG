'''
Given two images ("./front_01.jpeg") and ("./front_02.jpeg"), use SIFT to find the keypoints and stitch the images together. Save the stitched image as "front_stitched.jpeg". Note that "front_01.jpeg" is the left image and "front_02.jpeg" is the right image.
'''


import cv2
import numpy as np
import os
from typing import List

def read_images(image_paths: List[str]) -> List[np.ndarray]:
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        if img is None:
            raise ValueError(f"Image at path '{path}' could not be loaded.")
        images.append(img)
    return images

def detect_and_compute(images: List[np.ndarray]) -> List[np.ndarray]:
    keypoints_list = []
    descriptors_list = []
    # Initialize SIFT with fixed parameters
    sift = cv2.SIFT_create(
        nfeatures=0,
        nOctaveLayers=3,
        contrastThreshold=0.04,
        edgeThreshold=10,
        sigma=1.6
    )
    for img in images:
        keypoints, descriptors = sift.detectAndCompute(img, None)
        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)
    return keypoints_list, descriptors_list

def match_features(descriptors_list: List[np.ndarray]) -> List[List[cv2.DMatch]]:
    # FLANN parameters for SIFT descriptors
    index_params = dict(algorithm=1, trees=5)  # algorithm=1 for KDTree
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches_list = []
    for i in range(len(descriptors_list) - 1):
        matches = flann.knnMatch(descriptors_list[i], descriptors_list[i + 1], k=2)
        # Apply Lowe's ratio test
        good_matches = []
        ratio_thresh = 0.75
        for m, n in matches:
            if m.distance < ratio_thresh * n.distance:
                good_matches.append(m)
        matches_list.append(good_matches)
    return matches_list

def estimate_homographies(keypoints_list: List[List[cv2.KeyPoint]], matches_list: List[List[cv2.DMatch]]) -> List[np.ndarray]:
    homographies = []
    for i in range(len(matches_list)):
        src_pts = np.float32([keypoints_list[i][m.queryIdx].pt for m in matches_list[i]]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_list[i + 1][m.trainIdx].pt for m in matches_list[i]]).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        homographies.append(H)
    return homographies

def compute_cumulative_homographies(homographies: List[np.ndarray], ref_idx: int) -> List[np.ndarray]:
    cumulative_homographies = [np.eye(3)]
    # Left of reference image
    for i in range(ref_idx, 0, -1):
        H = homographies[i - 1]
        cumulative_homographies.insert(0, cumulative_homographies[0] @ H)
    # Right of reference image
    for i in range(ref_idx, len(homographies)):
        H = homographies[i]
        cumulative_homographies.append(cumulative_homographies[-1] @ np.linalg.inv(H))
    return cumulative_homographies

def warp_images(images: List[np.ndarray], cumulative_homographies: List[np.ndarray]) -> List[np.ndarray]:
    corners = []
    sizes = []
    for i, img in enumerate(images):
        h, w = img.shape[:2]
        # Image corners
        corners_img = np.array([
            [0, 0],
            [0, h],
            [w, h],
            [w, 0]
        ], dtype=np.float32).reshape(-1, 1, 2)
        # Warp corners
        warped_corners = cv2.perspectiveTransform(corners_img, cumulative_homographies[i])
        corners.append(warped_corners)
        sizes.append((w, h))
    return corners, sizes

def calculate_panorama_size(corners: List[np.ndarray]) -> tuple:
    all_corners = np.vstack(corners)
    [xmin, ymin] = np.int32(all_corners.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(all_corners.max(axis=0).ravel() + 0.5)
    panorama_size = (xmax - xmin, ymax - ymin)
    offset = (-xmin, -ymin)
    return panorama_size, offset

def warp_and_blend(images: List[np.ndarray], cumulative_homographies: List[np.ndarray]) -> np.ndarray:
    corners, sizes = warp_images(images, cumulative_homographies)
    panorama_size, offset = calculate_panorama_size(corners)
    # Initialize panorama canvas
    panorama = np.zeros((panorama_size[1], panorama_size[0], 3), dtype=np.uint8)
    masks = []
    warped_images = []
    for i, img in enumerate(images):
        h, w = img.shape[:2]
        # Offset translation
        translation = np.array([
            [1, 0, offset[0]],
            [0, 1, offset[1]],
            [0, 0, 1]
        ])
        warp_mat = translation @ cumulative_homographies[i]
        warped_img = cv2.warpPerspective(img, warp_mat, panorama_size)
        warped_images.append(warped_img)
        # Create mask
        mask = np.zeros((h, w), dtype=np.uint8)
        mask[:, :] = 255
        warped_mask = cv2.warpPerspective(mask, warp_mat, panorama_size)
        masks.append(warped_mask)
    # Blend images
    panorama = blend_images_multiband(warped_images, masks)
    return panorama

def blend_images_multiband(warped_images: List[np.ndarray], masks: List[np.ndarray]) -> np.ndarray:
    panorama = np.zeros_like(warped_images[0], dtype=np.float32)
    total_mask = np.zeros_like(masks[0], dtype=np.float32)
    for img, mask in zip(warped_images, masks):
        mask_normalized = mask.astype(np.float32) / 255.0
        img_float = img.astype(np.float32)
        panorama += img_float * mask_normalized[..., np.newaxis]
        total_mask += mask_normalized
    total_mask[total_mask == 0] = 1.0  # Avoid division by zero
    panorama = panorama / total_mask[..., np.newaxis]
    panorama = panorama.astype(np.uint8)
    return panorama

def create_panorama(image_paths: List[str]) -> np.ndarray:
    images = read_images(image_paths)
    keypoints_list, descriptors_list = detect_and_compute(images)
    matches_list = match_features(descriptors_list)
    homographies = estimate_homographies(keypoints_list, matches_list)
    # Reference index (middle image)
    ref_idx = len(images) // 2
    cumulative_homographies = compute_cumulative_homographies(homographies, ref_idx)
    panorama = warp_and_blend(images, cumulative_homographies)
    return panorama

def main():
    image_paths = ["front_01.jpeg", "front_02.jpeg"]
    panorama = create_panorama(image_paths)
    cv2.imwrite("front_stitched.jpeg", panorama)


def test():
    stitched = create_panorama(["front_01.jpeg", "front_02.jpeg"])
    result = cv2.imread("front_stitched.jpeg")

    # Resize both images to the same dimensions
    h, w = result.shape[:2]
    stitched_resized = cv2.resize(stitched, (w, h), interpolation=cv2.INTER_LINEAR)

    # Compare the resized images use mse
    mse = np.mean((result - stitched_resized) ** 2)
    threshold = 100  # Adjust based on acceptable error
    assert mse < threshold

    # clean up
    # os.remove("front_stitched.jpeg")


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")