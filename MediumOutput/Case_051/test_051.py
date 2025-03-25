'''
Given an image ("./test_image.png"), apply dynamic color filtering based on pixel brightness. For pixels with brightness above a certain threshold = 150, convert the region to grayscale, while leaving the rest of the image untouched. Save the result as "filtered_image.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path):
    return cv2.imread(image_path)

def generate_mask(image:np.ndarray, threshold:int):
    brightness = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(brightness, threshold, 255)
    
    return mask

def to_grayscale(image:np.ndarray):
    single_channel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.merge([single_channel, single_channel, single_channel])

def apply_mask(ori_image:np.ndarray, gray_image:np.ndarray, mask:np.ndarray):
    ori_image[np.where(mask == 255)] = gray_image[np.where(mask == 255)]
    return ori_image

def main():
    image_path = Path('./test_image.png')
    image = load_image(str(image_path))
    graysacle = to_grayscale(image)
    mask = generate_mask(image, 150)
    filtered_image = apply_mask(image, graysacle, mask)
    cv2.imwrite('filtered_image.png', filtered_image)

def test():
    image_path = Path('./test_image.png')
    image = load_image(str(image_path))
    graysacle = to_grayscale(image)
    mask = generate_mask(image, 150)
    filtered_image = apply_mask(image, graysacle, mask)
    # cv2.imwrite('filtered_image.png', filtered_image)
    assert os.path.exists('filtered_image.png')
    result = cv2.imread('filtered_image.png')

    assert np.array_equal(result, filtered_image)

    # clean up
    # os.remove('filtered_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')