'''
Given an image ("./test_image.png"), convert it to grayscale and apply region-based filtering (Gaussian Blur only on upper half), Gaussian Blur with a kernel size of 21x21 and sigmaX=11 (using GaussianBlur). Save the resulting image as "test_image_filtered.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path):
    return cv2.imread(str(image_path))

def cvt_to_gray(image:np.ndarray):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def region_based_filtering(image:np.ndarray):
    h, w = image.shape
    blurred = cv2.GaussianBlur(image[:h//2], (21, 21), 11)
    image[:h//2] = blurred

    return image

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)

    gray = cvt_to_gray(image)
    filtered = region_based_filtering(gray)
    cv2.imwrite('./test_image_filtered.png', filtered)

def test():
    assert Path('./test_image_filtered.png').exists()

    result = cv2.imread('./test_image_filtered.png', cv2.IMREAD_GRAYSCALE)
    image = load_image(Path('./test_image.png'))
    gray = cvt_to_gray(image)
    filtered = region_based_filtering(gray)

    assert np.array_equal(result, filtered)

    # cleanup
    # os.remove('./test_image_filtered.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')