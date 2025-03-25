'''
Given an image ("./test_image.png"), convert it to grayscale first, and divide it into four quadrants. Apply following operations to each quadrant: 1. Top-left quadrant: Apply Gaussian Blur to smooth the image (kernel size=3, sigmaX=5). 2. Top-right quadrant: Apply Sobel Edge Detection to highlight edges (kernel size=5). 3. Bottom-left quadrant: Apply Image Sharpening to enhance details (kernel=[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 4. Bottom-right quadrant: Apply Histogram Equalization to improve contrast. Save the resulting image as "test_image_processed.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path):
    return cv2.imread(str(image_path))

def cvt_to_gray(image:np.ndarray):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image:np.ndarray, kernel_size:int, sigmaX:float):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)

def apply_sobel_edge_detection(image:np.ndarray, kernel_size:int):
    return cv2.Sobel(image, cv2.CV_8U, 1, 1, ksize=kernel_size)

def apply_image_sharpening(image:np.ndarray, kernel:np.ndarray):
    return cv2.filter2D(image, -1, kernel)

def apply_histogram_equalization(image:np.ndarray):
    return cv2.equalizeHist(image)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)

    gray = cvt_to_gray(image)
    h, w = gray.shape

    top_left = gray[:h//2, :w//2]
    top_right = gray[:h//2, w//2:]
    bottom_left = gray[h//2:, :w//2]
    bottom_right = gray[h//2:, w//2:]

    top_left = apply_gaussian_blur(top_left, 3, 5)
    top_right = apply_sobel_edge_detection(top_right, 5)
    bottom_left = apply_image_sharpening(bottom_left, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
    bottom_right = apply_histogram_equalization(bottom_right)

    gray[:h//2, :w//2] = top_left
    gray[:h//2, w//2:] = top_right
    gray[h//2:, :w//2] = bottom_left
    gray[h//2:, w//2:] = bottom_right

    cv2.imwrite('./test_image_processed.png', gray)

def test():
    assert Path('./test_image_processed.png').exists()

    result = cv2.imread('./test_image_processed.png', cv2.IMREAD_GRAYSCALE)
    image = load_image(Path('./test_image.png'))
    gray = cvt_to_gray(image)
    h, w = gray.shape

    top_left = gray[:h//2, :w//2]
    top_right = gray[:h//2, w//2:]
    bottom_left = gray[h//2:, :w//2]
    bottom_right = gray[h//2:, w//2:]

    top_left = apply_gaussian_blur(top_left, 3, 5)
    top_right = apply_sobel_edge_detection(top_right, 5)
    bottom_left = apply_image_sharpening(bottom_left, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
    bottom_right = apply_histogram_equalization(bottom_right)

    gray[:h//2, :w//2] = top_left
    gray[:h//2, w//2:] = top_right
    gray[h//2:, :w//2] = bottom_left
    gray[h//2:, w//2:] = bottom_right

    assert np.array_equal(result, gray)

    # cleanup
    # os.remove('./test_image_processed.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')