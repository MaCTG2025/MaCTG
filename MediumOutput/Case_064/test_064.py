'''
Given an image ("./test_image.png"), scale it up and down by a factor of 2. And export histograms of original and scaled images, save the histograms as "original_hist.npy", "upscaled_hist.npy" and "downscaled_hist.npy".
'''

import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def rescale_image(image:np.ndarray, scale:float, interpolation:int) -> np.ndarray:
    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=interpolation)

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def calculate_histogram(image:np.ndarray) -> np.ndarray:
    return cv2.calcHist([image], [0], None, [256], [0, 256])

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # rescale using different interpolation methods
    up_scaled = rescale_image(image, 2, cv2.INTER_LINEAR)
    down_scaled = rescale_image(image, 0.5, cv2.INTER_LINEAR)
    
    # convert to grayscale
    gray_image = convert_to_grayscale(image)
    gray_up_scaled = convert_to_grayscale(up_scaled)
    gray_down_scaled = convert_to_grayscale(down_scaled)
    
    # calculate histograms
    original_hist = calculate_histogram(gray_image)
    up_scaled_hist = calculate_histogram(gray_up_scaled)
    down_scaled_hist = calculate_histogram(gray_down_scaled)
    
    # save the results
    np.save('original_hist.npy', original_hist)
    np.save('up_scaled_hist.npy', up_scaled_hist)
    np.save('down_scaled_hist.npy', down_scaled_hist)

def test():
    assert Path('original_hist.npy').exists()
    assert Path('up_scaled_hist.npy').exists()
    assert Path('down_scaled_hist.npy').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    up_scaled = rescale_image(image, 2, cv2.INTER_LINEAR)
    down_scaled = rescale_image(image, 0.5, cv2.INTER_LINEAR)
    
    # convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_up_scaled = cv2.cvtColor(up_scaled, cv2.COLOR_BGR2GRAY)
    gray_down_scaled = cv2.cvtColor(down_scaled, cv2.COLOR_BGR2GRAY)
    
    # load the histograms
    original_hist = np.load('original_hist.npy')
    up_scaled_hist = np.load('up_scaled_hist.npy')
    down_scaled_hist = np.load('down_scaled_hist.npy')
    
    # calculate the histograms
    original_hist_test = calculate_histogram(gray_image)
    up_scaled_hist_test = calculate_histogram(gray_up_scaled)
    down_scaled_hist_test = calculate_histogram(gray_down_scaled)
    
    # assert that the histograms are the same
    assert np.array_equal(original_hist, original_hist_test)
    assert np.array_equal(up_scaled_hist, up_scaled_hist_test)
    assert np.array_equal(down_scaled_hist, down_scaled_hist_test)

    # clean up
    # os.remove('original_hist.npy')
    # os.remove('up_scaled_hist.npy')
    # os.remove('down_scaled_hist.npy')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')
