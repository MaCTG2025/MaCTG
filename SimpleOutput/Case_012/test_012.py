'''
Given an input image ("./test_image.png"), compute the Histogram of Oriented Gradients (HOG) for the image and save the result as \"hog.npy\". Use the following parameters: cell_size=(8, 8), block_size=(2, 2), nbins=9.
'''

import cv2
from PIL import Image
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(image_path)

def compute_hog(image:np.ndarray, cell_size:tuple, block_size:tuple, nbins:int)->np.ndarray:
    hog = cv2.HOGDescriptor(_winSize=(image.shape[1]//cell_size[1]*cell_size[1], image.shape[0]//cell_size[0]*cell_size[0]),
                            _blockSize=(block_size[1]*cell_size[1], block_size[0]*cell_size[0]),
                            _blockStride=(cell_size[1], cell_size[0]),
                            _cellSize=(cell_size[1], cell_size[0]),
                            _nbins=nbins)
    return hog.compute(image)

def save_hog(hog:np.ndarray, save_path:Path):
    np.save(save_path, hog)

def main():
    image_path = Path("./test_image.png")
    save_path = Path("./hog.npy")
    cell_size = (8, 8)
    block_size = (2, 2)
    nbins = 9

    image = load_image(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hog = compute_hog(image, cell_size, block_size, nbins)
    save_hog(hog, save_path)

def test():
    save_path = Path("./hog.npy")
    assert save_path.exists(), f"{save_path} does not exist"
    res = np.load(save_path)
    
    input_image = cv2.imread("./test_image.png")
    image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    cell_size = (8, 8)
    block_size = (2, 2)
    nbins = 9
    hog = compute_hog(image, cell_size, block_size, nbins)

    assert np.array_equal(hog, res), f"Expected {hog} but got {res}"

    # cleanup
    # os.remove(save_path)


if __name__=="__main__":
    # main()
    test()
    print("All tests passed.")