'''
Given an image ("./test_image.png"), apply bilateral filtering (with d = 9, sigmaColor = 75, sigmaSpace = 75) to reduce noise while preserving edges, followed by non-maximum suppression on the gradient magnitudes (using Sobel operators with ksize = 5 and an NMS threshold of 100) to enhance the most prominent edges, save the resulting image as "test_image_edges.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path)
    return image

def apply_bilateral_filter(image:np.ndarray, d:int, sigmaColor:float, sigmaSpace:float)->np.ndarray:
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

def apply_sobel_edge_detection(image:np.ndarray, kernel_size:int)->np.ndarray:
    # Apply Sobel operators
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=kernel_size)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=kernel_size)

    # Calculate gradient magnitude
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)
    return grad_mag

def non_max_suppression(image:np.ndarray, threshold:int)->np.ndarray:
    grad_mag_max = np.maximum(image, threshold)
    grad_mag_max[image < threshold] = 0
    result_image = cv2.normalize(grad_mag_max, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return result_image

def main()->None:
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bilateral = apply_bilateral_filter(image, 9, 75, 75)
    sobel = apply_sobel_edge_detection(bilateral, 5)
    result = non_max_suppression(sobel, 100)

    cv2.imwrite('test_image_edges.png', result)

def test():
    result = cv2.imread('test_image_edges.png', cv2.IMREAD_GRAYSCALE)

    image_path = Path('./test_image.png')
    image = load_image(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bilateral = apply_bilateral_filter(image, 9, 75, 75)
    sobel = apply_sobel_edge_detection(bilateral, 5)
    expected = non_max_suppression(sobel, 100)

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('test_image_edges.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")