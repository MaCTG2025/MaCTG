'''
Given an image ("./test_image.png"), apply a sharpening filter of the following values: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]. Then apply a 5x5 gaussian filter with sigmax=5 (using GaussianBlur). Save the resulting image as "sharpened_gaussian_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_sharpening_filter(image:np.ndarray) -> np.ndarray:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    return cv2.filter2D(image, -1, kernel)

def apply_gaussian_filter(image:np.ndarray, kernel_size:int, sigmaX:float) -> np.ndarray:
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    sharpened_image = apply_sharpening_filter(image)
    sharpened_gaussian_image = apply_gaussian_filter(sharpened_image, 5, 5)
    cv2.imwrite('sharpened_gaussian_image.png', sharpened_gaussian_image)

def test():
    assert Path('sharpened_gaussian_image.png').exists()

    image = load_image(Path('./test_image.png'))
    sharpened_image = apply_sharpening_filter(image)
    sharpened_gaussian_image = apply_gaussian_filter(sharpened_image, 5, 5)
    result = cv2.imread('sharpened_gaussian_image.png')

    assert np.array_equal(sharpened_gaussian_image, result)

    # clean up
    # os.remove('sharpened_gaussian_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')