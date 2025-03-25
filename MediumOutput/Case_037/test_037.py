'''
Given an image ("./test_image.png"), convert to grayscale and apply adaptive thresholding (blockSize = 71, C = 2) for binarization. Finally detect contours of the binarized image and draw it in red (thickness=2). Save the resulting image as "adaptive_threshold_contours.png".
'''

import cv2
from pathlib import Path
import os
import numpy as np

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_adaptive_threshold(image:np.ndarray, blockSize:int, C:int) -> np.ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)

def find_contours(image:np.ndarray) -> np.ndarray:
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
    return image

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    threshold_image = apply_adaptive_threshold(image, 71, 2)
    contours_image = find_contours(threshold_image)
    cv2.imwrite('adaptive_threshold_contours.png', contours_image)

def test():
    assert Path('adaptive_threshold_contours.png').exists()

    image = load_image(Path('./test_image.png'))
    threshold_image = apply_adaptive_threshold(image, 71, 2)
    contours_image = find_contours(threshold_image)
    result = cv2.imread('adaptive_threshold_contours.png')

    assert np.array_equal(contours_image, result)

    # clean up
    # os.remove('adaptive_threshold_contours.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')