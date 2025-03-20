'''
Given an input image ("./test_image.png"), apply a bilateral filter to smooth the image while preserving edges (Use a d=9, sigmaColor=75, sigmaSpace=75). Save the resulting image as bilateral_filtered_image.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_bilateral_filter(image:np.ndarray) -> np.ndarray:
    return cv2.bilateralFilter(image, 9, 75, 75)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    bilateral_filtered_image = apply_bilateral_filter(image)
    
    cv2.imwrite('bilateral_filtered_image.png', bilateral_filtered_image)

def test():
    assert Path('bilateral_filtered_image.png').exists()
    
    image = cv2.imread('test_image.png')
    bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
    
    assert np.array_equal(cv2.imread('bilateral_filtered_image.png'), bilateral_filtered_image)
    
    # cleanup
    # os.remove('bilateral_filtered_image.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")