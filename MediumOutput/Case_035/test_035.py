'''
Given an image ("./test_image.png"), apply a 3x3 gaussian filter with sigmax=5(using GaussianBlur) and perform Canny edge detection (thresholds 100, 200). Save the resulting image as "canny_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_gaussian_filter(image:np.ndarray, kernel_size:int, sigmaX:float) -> np.ndarray:
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)

def canny_edge_detection(image:np.ndarray, threshold1:int, threshold2:int) -> np.ndarray:
    return cv2.Canny(image, threshold1, threshold2)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    blurred_image = apply_gaussian_filter(image, 3, 5)
    canny_image = canny_edge_detection(blurred_image, 100, 200)
    cv2.imwrite('canny_image.png', canny_image)

def test():
    assert Path('canny_image.png').exists()

    image = load_image(Path('./test_image.png'))
    blurred_image = apply_gaussian_filter(image, 3, 5)
    canny_image = canny_edge_detection(blurred_image, 100, 200)
    result = cv2.imread('canny_image.png', cv2.IMREAD_GRAYSCALE)
    
    assert np.array_equal(canny_image, result)

    # clean up
    # os.remove('canny_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')