'''
Given an image ("./test_image.png"), rotate it by 180 degrees, then detect its contours, and draw the contours in red (thickness=3). Finally, save the resulting image as "rotated_contours.png".
'''


import cv2
from pathlib import Path
import os
import numpy as np


def rotate_image(image_path:Path) -> np.ndarray:
    image = cv2.imread(str(image_path))
    rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    return rotated_image

def find_contours(image:np.ndarray) -> np.ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binarized_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binarized_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
    return image

def main():
    image_path = Path('./test_image.png')
    rotated_image = rotate_image(image_path)
    image = find_contours(rotated_image)
    cv2.imwrite('rotated_contours.png', image)

def test():
    assert Path('rotated_contours.png').exists()

    # load the rotated contours image
    result = cv2.imread('rotated_contours.png')
    rotated_contours_array = find_contours(rotate_image(Path('./test_image.png')))
    
    assert np.array_equal(rotated_contours_array, result)

    # clean up
    # os.remove('rotated_contours.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')