'''
Given an input image ("./test_image.png"), apply Contrast Limited Adaptive Histogram Equalization (CLAHE) to enhance the contrast of the image (use clipLimit=2.0 and tileGridSize=(8, 8)), and save the result as clahe_image.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_clahe(image:np.ndarray, clipLimit:float, tileGridSize:tuple) -> np.ndarray:
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    return clahe.apply(image)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    image = convert_to_grayscale(image)
    
    clahe_image = apply_clahe(image, 2.0, (8, 8))
    
    cv2.imwrite('clahe_image.png', clahe_image)

def test():
    assert Path('clahe_image.png').exists()
    
    image = cv2.imread('test_image.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image)
    
    assert np.array_equal(cv2.imread('clahe_image.png', cv2.IMREAD_GRAYSCALE), clahe_image)
    
    # cleanup
    # os.remove('clahe_image.png')

if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")