'''
Given an image ("./test_image.png"), rescale using different interpolation methods (Linear, Cubic, Area), calculate pixel intensity differences between rescaled images, and save the results into npy files as "diff_linear_cubic.npy", "diff_cubic_area.npy", and "diff_area_linear.npy".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def rescale_image(image:np.ndarray, scale:float, interpolation:int) -> np.ndarray:
    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=interpolation)

def calculate_pixel_intensity_difference(image1:np.ndarray, image2:np.ndarray) -> np.ndarray:
    return cv2.absdiff(image1, image2)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # rescale using different interpolation methods
    linear_rescaled = rescale_image(image, 2, cv2.INTER_LINEAR)
    cubic_rescaled = rescale_image(image, 2, cv2.INTER_CUBIC)
    area_rescaled = rescale_image(image, 2, cv2.INTER_AREA)

    # calculate pixel intensity differences
    diff_linear_cubic = calculate_pixel_intensity_difference(linear_rescaled, cubic_rescaled)
    diff_cubic_area = calculate_pixel_intensity_difference(cubic_rescaled, area_rescaled)
    diff_area_linear = calculate_pixel_intensity_difference(area_rescaled, linear_rescaled)

    # save the results
    np.save('diff_linear_cubic.npy', diff_linear_cubic)
    np.save('diff_cubic_area.npy', diff_cubic_area)
    np.save('diff_area_linear.npy', diff_area_linear)

def test():
    assert Path('diff_linear_cubic.npy').exists()
    assert Path('diff_cubic_area.npy').exists()
    assert Path('diff_area_linear.npy').exists()

    # load the images
    image = cv2.imread('test_image.png')
    linear_rescaled = rescale_image(image, 2, cv2.INTER_LINEAR)
    cubic_rescaled = rescale_image(image, 2, cv2.INTER_CUBIC)
    area_rescaled = rescale_image(image, 2, cv2.INTER_AREA)

    # load the differences
    diff_linear_cubic = np.load('diff_linear_cubic.npy')
    diff_cubic_area = np.load('diff_cubic_area.npy')
    diff_area_linear = np.load('diff_area_linear.npy')

    # calculate the differences
    diff_linear_cubic_test = calculate_pixel_intensity_difference(linear_rescaled, cubic_rescaled)
    diff_cubic_area_test = calculate_pixel_intensity_difference(cubic_rescaled, area_rescaled)
    diff_area_linear_test = calculate_pixel_intensity_difference(area_rescaled, linear_rescaled)

    # assert that the differences are the same
    assert np.array_equal(diff_linear_cubic, diff_linear_cubic_test)
    assert np.array_equal(diff_cubic_area, diff_cubic_area_test)
    assert np.array_equal(diff_area_linear, diff_area_linear_test)

    # clean up
    # os.remove('diff_linear_cubic.npy')
    # os.remove('diff_cubic_area.npy')
    # os.remove('diff_area_linear.npy')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')