'''
Given an image ("./test_image.png"), convert to HSV, modify the Hue channel (+50), convert back to RGB, and save the resulting image as "hue_modified_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_hsv(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def modify_hue(image:np.ndarray) -> np.ndarray:
    hsv_image = convert_to_hsv(image)
    hsv_image[..., 0] += 50
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    modified_image = modify_hue(image)
    cv2.imwrite('hue_modified_image.png', modified_image)

def test(): 
    assert Path('hue_modified_image.png').exists()

    image = load_image(Path('./test_image.png'))
    modified_image = modify_hue(image)
    result = cv2.imread('hue_modified_image.png')

    assert np.array_equal(modified_image, result)

    # clean up
    # os.remove('hue_modified_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')
