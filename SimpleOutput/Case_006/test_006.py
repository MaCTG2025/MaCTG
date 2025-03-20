'''
Given an input image ("./test_image.png"), add a sharpening filter to it. The sharpening filter is a 3*3 matrix with the following values: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]. Save the resulting image as "sharpened_image.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def apply_filter(image:np.ndarray)->np.ndarray:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    return cv2.filter2D(image, -1, kernel)

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    filtered_image = apply_filter(image)
    save_image(filtered_image, Path('./sharpened_image.png'))

def test():
    assert Path('sharpened_image.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    filtered = apply_filter(original)

    # load the image with corners
    filtered_result = cv2.imread('sharpened_image.png')

    assert np.array_equal(filtered, filtered_result)

    # clean up
    # os.remove('sharpened_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')