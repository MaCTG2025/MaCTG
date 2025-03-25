'''
Given ("./water_coins.jpg"), develop an image segmentation algorithm using the Watershed method to segment an image into distinct regions based on intensity gradients, handling over-segmentation with markers, save the segmented image as "water_coins_segmented.png".
'''


import cv2
import numpy as np
from typing import List
import os


def load_image(image_path: str) -> np.ndarray:
    return cv2.imread(image_path)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def binarize(image: np.ndarray) -> np.ndarray:
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def remove_noise(image: np.ndarray) -> np.ndarray:
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=2)
    return opening

def get_bg_and_fg(image: np.ndarray) -> tuple:
    sure_bg = cv2.dilate(image, np.ones((3, 3), np.uint8), iterations=3)
    dist_transform = cv2.distanceTransform(image, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    return sure_bg, sure_fg, unknown

def get_markers(sure_fg: np.ndarray, unknown: np.ndarray) -> np.ndarray:
    _, markers = cv2.connectedComponents(sure_fg)
    markers += 1
    markers[unknown == 255] = 0
    return markers

def apply_watershed(image: np.ndarray, markers: np.ndarray) -> np.ndarray:
    return cv2.watershed(image, markers)

def visualize_boundaries(image: np.ndarray, markers: np.ndarray) -> np.ndarray:
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image[markers == -1] = [0, 0, 255]
    return image

def watershed_segmentation(image_path: str) -> np.ndarray:
    image = load_image(image_path)
    image_gs = convert_to_grayscale(image)
    binary = binarize(image_gs)
    opening = remove_noise(binary)
    sure_bg, sure_fg, unknown = get_bg_and_fg(opening)
    markers = get_markers(sure_fg, unknown)
    segmented = apply_watershed(cv2.imread(image_path), markers)
    return visualize_boundaries(image, markers)

def main() -> None:
    image_path = "water_coins.jpg"
    segmented = watershed_segmentation(image_path)
    cv2.imwrite("water_coins_segmented.png", segmented)

def test():
    assert os.path.exists("water_coins_segmented.png")

    image_path = "water_coins.jpg"
    segmented = watershed_segmentation(image_path)

    result = cv2.imread("water_coins_segmented.png")

    assert np.allclose(segmented, result)

    # Clean up
    # os.remove("water_coins_segmented.png")

if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")