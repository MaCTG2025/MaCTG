'''
Given an input image ("./test_image.png"), convert it to the LAB color space and save the resulting image as "lab_image.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_lab(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    lab_image = convert_to_lab(image)
    
    cv2.imwrite('lab_image.png', lab_image)

def test():
    assert Path('lab_image.png').exists()
    
    image = cv2.imread('test_image.png')
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    assert np.array_equal(cv2.imread('lab_image.png'), lab_image)
    
    # cleanup
    # os.remove('lab_image.png')

if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")
