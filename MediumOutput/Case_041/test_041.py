'''
Given an image ("./test_image.png"), Apply an affine transformation (45° rotation, 1.2x scaling, and translation by (50, 30) pixels) to the image, then perform Harris corner detection on both the original and transformed images with a block size of 2 and a ksize of 3. Save the resulting images as "harris_original.png" and "harris_transformed.png".
'''

import cv2
from pathlib import Path
import os
import numpy as np

def affine_transformation(image:np.ndarray, angle:int, scale:float, translation:tuple) -> np.ndarray:
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, scale)
    M[:, 2] += translation
    return cv2.warpAffine(image, M, (cols, rows))

def harris_corner_detection(image:np.ndarray, block_size:int, ksize:int) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, block_size, ksize, 0.04)
    image[dst > 0.01 * dst.max()] = [0, 0, 255]
    return image

def main():
    image_path = Path('./test_image.png')
    image = cv2.imread(str(image_path))
    transformed_image = affine_transformation(image, 45, 1.2, (50, 30))
    harris_original = harris_corner_detection(image.copy(), 2, 3)
    harris_transformed = harris_corner_detection(transformed_image.copy(), 2, 3)
    cv2.imwrite('harris_original.png', harris_original)
    cv2.imwrite('harris_transformed.png', harris_transformed)

def test():
    assert Path('harris_original.png').exists()
    assert Path('harris_transformed.png').exists()

    image = cv2.imread('test_image.png')
    transformed_image = affine_transformation(image, 45, 1.2, (50, 30))
    harris_original = harris_corner_detection(image.copy(), 2, 3)
    harris_transformed = harris_corner_detection(transformed_image.copy(), 2, 3)

    assert np.array_equal(harris_original, cv2.imread('harris_original.png'))
    assert np.array_equal(harris_transformed, cv2.imread('harris_transformed.png'))

    # clean up
    # os.remove('harris_original.png')
    # os.remove('harris_transformed.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')