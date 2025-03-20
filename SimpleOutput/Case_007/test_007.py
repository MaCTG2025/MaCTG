'''
Given an input image ("./test_image.png"), first convert it to graysacle. Then binarize the image using a threshold value of 128. Finally, find the contours in the binarized image, draw it in red (thickness=2) and save the resulting image as "contours_image.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray)->np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def binarize(image:np.ndarray)->np.ndarray:
    _, binarized = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return binarized

def find_contours(image:np.ndarray)->np.ndarray:
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image:np.ndarray, contours:np.ndarray)->np.ndarray:
    return cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    grayscale = convert_to_grayscale(image)
    binarized = binarize(grayscale)
    contours = find_contours(binarized)
    image_with_contours = draw_contours(image.copy(), contours)
    save_image(image_with_contours, Path('./contours_image.png'))

def test():
    assert Path('contours_image.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    grayscale = convert_to_grayscale(original)
    binarized = binarize(grayscale)
    contours = find_contours(binarized)
    image_with_contours = draw_contours(original, contours)

    # load the image with corners
    image_with_contours_result = cv2.imread('contours_image.png')

    assert np.array_equal(image_with_contours, image_with_contours_result)

    # clean up
    # os.remove('contours_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')