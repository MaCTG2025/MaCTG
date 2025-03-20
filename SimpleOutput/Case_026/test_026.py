'''
Given an input image ("./test_image.png"), convert it to the YUV color space and save the resulting image as yuv_image.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_yuv(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    yuv_image = convert_to_yuv(image)
    
    cv2.imwrite('yuv_image.png', yuv_image)


def test():
    assert Path('yuv_image.png').exists()
    
    image = cv2.imread('test_image.png')
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    assert np.array_equal(cv2.imread('yuv_image.png'), yuv_image)
    
    # cleanup
    # os.remove('yuv_image.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")