'''
Given an input image ("./test_image.png"), convert it into grayscale first, apply adaptive thresholding to convert it into a binary image( use cv2.ADAPTIVE_THRESH_GAUSSIAN_C and cv2.THRESH_BINARY_INV with blockSize=11 and C=2), and save the resulting image as "binary_image.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_adaptive_threshold(image:np.ndarray, blockSize:int, C:int) -> np.ndarray:
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, blockSize, C)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    image = convert_to_grayscale(image)
    
    binary_image = apply_adaptive_threshold(image, 11, 2)
    
    cv2.imwrite('binary_image.png', binary_image)

def test():
    assert Path('binary_image.png').exists()
    
    image = cv2.imread('test_image.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    assert np.array_equal(cv2.imread('binary_image.png', cv2.IMREAD_GRAYSCALE), binary_image)
    
    # cleanup
    # os.remove('binary_image.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")