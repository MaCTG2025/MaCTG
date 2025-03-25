'''
Given an image ("./test_image.png"), apply multiple filters, first median (kernel size = 5) then fast mean denoising (h = 10, templateWindowSize = 7, searchWindowSize = 21). Save results as "final_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_median_filter(image:np.ndarray, kernel_size:int) -> np.ndarray:
    return cv2.medianBlur(image, kernel_size)

def apply_fast_mean_denoising(image:np.ndarray, h:int, templateWindowSize:int, searchWindowSize:int) -> np.ndarray:
    return cv2.fastNlMeansDenoising(image, None, h, templateWindowSize, searchWindowSize)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    median_image = apply_median_filter(image, 5)
    final_image = apply_fast_mean_denoising(median_image, 10, 7, 21)
    cv2.imwrite('final_image.png', final_image)

def test():
    assert Path('final_image.png').exists()

    image = load_image(Path('./test_image.png'))
    median_image = apply_median_filter(image, 5)
    final_image = apply_fast_mean_denoising(median_image, 10, 7, 21)
    result = cv2.imread('final_image.png')

    assert np.array_equal(final_image, result)

    # clean up
    # os.remove('final_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')