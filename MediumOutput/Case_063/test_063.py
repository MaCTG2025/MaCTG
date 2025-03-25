'''
Given an image ("./test_image.png"), add Gaussian noise with mean 0 and standard deviation 25, apply median filtering with kernel size 5x5, and detect corners using Harris corner detection. Save the resulting image as "test_image_corners.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

def add_gaussian_noise(image:np.ndarray, mean:float, std:float)->np.ndarray:
    noise = np.random.normal(mean, std, image.shape)
    noisy = image + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def apply_median_filter(image:np.ndarray, kernel_size:int)->np.ndarray:
    return cv2.medianBlur(image, kernel_size)

def detect_corners(image:np.ndarray, block_size:int, ksize:int, k:float)->np.ndarray:
    gray = np.float32(image)
    return cv2.cornerHarris(gray, block_size, ksize, k)

def main()->None:
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    noisy = add_gaussian_noise(image, 0, 25)
    median = apply_median_filter(noisy, 5)
    corners = detect_corners(median, 2, 3, 0.04)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image[corners>0.01*corners.max()] = [0, 0, 255]
    cv2.imwrite('test_image_corners.png', image)

def test():
    result = cv2.imread('test_image_corners.png')

    image_path = Path('./test_image.png')
    image = load_image(image_path)
    noisy = add_gaussian_noise(image, 0, 25)
    median = apply_median_filter(noisy, 5)
    corners = detect_corners(median, 2, 3, 0.04)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image[corners>0.01*corners.max()] = [0, 0, 255]
    expected = image

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('test_image_corners.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")