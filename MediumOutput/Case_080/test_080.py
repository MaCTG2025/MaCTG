'''
Given an image ("./test_image.png"), convert to grayscale, apply histogram equalization, and save original histogram and equalized histogram as "original_histogram.npy" and "equalized_histogram.npy", respectively.
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_grayscale(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_histogram_equalization(image:np.ndarray) -> np.ndarray:
    return cv2.equalizeHist(image)

def compute_histogram(image:np.ndarray) -> np.ndarray:
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # convert the image to grayscale
    gray = convert_to_grayscale(image)
    
    # apply histogram equalization
    equalized = apply_histogram_equalization(gray)
    
    # compute histograms
    original_hist = compute_histogram(gray)
    equalized_hist = compute_histogram(equalized)
    
    np.save('original_histogram.npy', original_hist)
    np.save('equalized_histogram.npy', equalized_hist)

def test():
    assert Path('original_histogram.npy').exists()
    assert Path('equalized_histogram.npy').exists()
    
    # load the histograms
    original_hist = np.load('original_histogram.npy')
    equalized_hist = np.load('equalized_histogram.npy')
    
    # assert that the histograms are not the same
    assert not np.array_equal(original_hist, equalized_hist)
    
    # clean up
    # os.remove('original_histogram.npy')
    # os.remove('equalized_histogram.npy')

if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")