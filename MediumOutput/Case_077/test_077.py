'''
Given an image ("./test_image.png"), convert it to grayscale, apply a brightness threshold (threshold_value = 200) to separate bright and dark regions, apply Gaussian blur (kernel size = (5, 5)) only to the bright regions,  and combine the blurred bright regions with the original dark regions, save the final image as "bright_regions.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_brightness_threshold(image:np.ndarray, threshold_value:int) -> np.ndarray:
    _, thresh = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh

def apply_gaussian_blur(image:np.ndarray, kernel_size:tuple) -> np.ndarray:
    return cv2.GaussianBlur(image, kernel_size, 0)

def combine_images(image1:np.ndarray, image2:np.ndarray) -> np.ndarray:
    return cv2.bitwise_or(image1, image2)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # convert the image to grayscale
    gray = convert_to_grayscale(image)
    
    # apply brightness threshold
    bright_regions = apply_brightness_threshold(gray, 200)
    
    # apply Gaussian blur to the bright regions
    bright_blurred = apply_gaussian_blur(bright_regions, (5, 5))
    
    # combine the blurred bright regions with the original dark regions
    result = combine_images(bright_blurred, gray)
    
    cv2.imwrite('bright_regions.png', result)

def test():
    assert Path('bright_regions.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('bright_regions.png', cv2.IMREAD_GRAYSCALE)
    
    # convert the image to grayscale
    gray = convert_to_grayscale(image)
    
    # apply brightness threshold
    bright_regions = apply_brightness_threshold(gray, 200)
    
    # apply Gaussian blur to the bright regions
    bright_blurred = apply_gaussian_blur(bright_regions, (5, 5))
    
    # combine the blurred bright regions with the original dark regions
    result_test = combine_images(bright_blurred, gray)
    
    # assert that the images are the same
    assert np.allclose(result, result_test)

    # clean up
    # os.remove('bright_regions.png')

if __name__ == '__main__':
    main()
    test()
    print('All tests passed')