'''
Given an input image ("./test_image.png"), convert it to grayscale, apply the Sobel operator to detect horizontal and vertical edges (kernel size=3), and save the resulting edge map as sobel_edges.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_sobel(image:np.ndarray) -> np.ndarray:
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    return np.sqrt(sobel_x**2 + sobel_y**2)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    image = convert_to_grayscale(image)
    
    sobel_edges = apply_sobel(image).astype(np.uint8)
    
    cv2.imwrite('sobel_edges.png', sobel_edges)

def test():
    assert Path('sobel_edges.png').exists()
    
    image = cv2.imread('test_image.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)
    
    assert np.array_equal(cv2.imread('sobel_edges.png', cv2.IMREAD_GRAYSCALE), sobel_edges.astype(np.uint8))
    
    # cleanup
    # os.remove('sobel_edges.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")