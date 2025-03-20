'''
Given an input image ("./test_image.png"), apply the morphological gradient operation, which highlights the difference between the dilation and erosion of an image. (Use a 5x5 kernel with cv2.MORPH_RECT shape). Save the resulting image as morphological_gradient.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_morphological_gradient(image:np.ndarray, kernel:np.ndarray) -> np.ndarray:
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morphological_gradient_image = apply_morphological_gradient(image, kernel)
    
    cv2.imwrite('morphological_gradient.png', morphological_gradient_image)

def test():
    assert Path('morphological_gradient.png').exists()
    
    image = cv2.imread('test_image.png')
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morphological_gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    
    assert np.array_equal(cv2.imread('morphological_gradient.png'), morphological_gradient_image)
    
    # cleanup
    # os.remove('morphological_gradient.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")