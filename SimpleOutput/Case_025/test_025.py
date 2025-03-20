'''
Given an input image ("./4star.jpg"), analyze the image to detect vertical symmetry. Highlight the axis of symmetry (if detected) by drawing a vertical green line down the middle of the image. Save the resulting image as symmetry_detected.png.
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def detect_vertical_symmetry(image:np.ndarray) -> np.ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    
    # get the left and right halves of the image
    left_half = gray_image[:, :width//2]
    right_half = gray_image[:, width//2:]
    
    # flip the right half
    right_half_flipped = cv2.flip(right_half, 1)
    
    # calculate the difference between the left and right halves
    diff = cv2.absdiff(left_half, right_half_flipped)
    
    if np.sum(diff) == 0:
        # vertical symmetry detected
        cv2.line(image, (width//2, 0), (width//2, height), (0, 255, 0), 2)

    return image

def main():
    image_path = Path('./4star.jpg')
    image = load_image(image_path)
    
    symmetry_image = detect_vertical_symmetry(image)
    
    cv2.imwrite('symmetry_detected.png', symmetry_image)

def test():
    assert Path('symmetry_detected.png').exists()
    
    image = cv2.imread('4star.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    
    left_half = gray_image[:, :width//2]
    right_half = gray_image[:, width//2:]
    right_half_flipped = cv2.flip(right_half, 1)
    diff = cv2.absdiff(left_half, right_half_flipped)
    
    if np.sum(diff) == 0:
        cv2.line(image, (width//2, 0), (width//2, height), (0, 255, 0), 2)
    
    assert np.array_equal(cv2.imread('symmetry_detected.png'), image)
    
    # cleanup
    # os.remove('symmetry_detected.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")