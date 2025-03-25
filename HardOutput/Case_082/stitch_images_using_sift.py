import cv2
import numpy as np

def stitch_images_using_sift(image_left_path: str, image_right_path: str, output_path: str) -> None:
    """
    Stitches two images together using the SIFT (Scale-Invariant Feature Transform) algorithm and saves the result.

    This function takes the file paths of two images (left and right) and uses the SIFT algorithm to detect keypoints
    and compute descriptors. It then matches the keypoints between the two images, computes a homography matrix,
    and warps the right image to align with the left image. Finally, it stitches the two images together and saves
    the result to the specified output path.

    Parameters:
    -----------
    image_left_path : str
        The file path of the left image (e.g., "./front_01.jpeg").
    image_right_path : str
        The file path of the right image (e.g., "./front_02.jpeg").
    output_path : str
        The file path where the stitched image will be saved (e.g., "front_stitched.jpeg").

    Returns:
    --------
    None
        The function does not return any value. It saves the stitched image to the specified output path.

    Requirements:
    -------------
    - The left image (image_left_path) should be the image on the left side of the final stitched image.
    - The right image (image_right_path) should be the image on the right side of the final stitched image.
    - Both images should be in a format supported by OpenCV (e.g., JPEG, PNG).
    - The output_path should include the desired file name and extension for the stitched image.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing and SIFT keypoint detection.
    - NumPy (numpy) for numerical operations and matrix manipulations.

    Example:
    --------
    stitch_images_using_sift("./front_01.jpeg", "./front_02.jpeg", "front_stitched.jpeg")
    """
    # Load the images
    img1 = cv2.imread(image_left_path)
    img2 = cv2.imread(image_right_path)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Find keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    # Use FlannBasedMatcher
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Find matches
    matches = flann.knnMatch(des1, des2, k=2)

    # Apply Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Check if enough matches are found
    if len(good_matches) < 4:
        raise ValueError("Not enough good matches to compute homography.")

    # Extract matched points
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Compute homography using RANSAC
    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

    # Get dimensions of images
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # Transform corners of img2 to determine output size
    pts = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    transformed_pts = cv2.perspectiveTransform(pts, H)

    # Combine corners from both images
    all_corners = np.concatenate((transformed_pts.reshape(-1, 2), np.float32([[0, 0], [w1, 0], [0, h1], [w1, h1]])), axis=0)

    # Compute bounding box
    x_min, y_min = np.int32(all_corners.min(axis=0))
    x_max, y_max = np.int32(all_corners.max(axis=0))

    # Compute output size
    output_width = x_max - x_min
    output_height = y_max - y_min

    # Adjust homography to include translation
    translation_matrix = np.array([[1, 0, -x_min], [0, 1, -y_min], [0, 0, 1]])
    adjusted_H = translation_matrix.dot(H)

    # Warp the right image with adjusted homography
    stitched = cv2.warpPerspective(img2, adjusted_H, (output_width, output_height))

    # Place the left image into the stitched image
    stitched[-y_min:h1 - y_min, -x_min:w1 - x_min] = img1

    # Save the stitched image
    cv2.imwrite(output_path, stitched)