'''
Given an image ("./test_image.png"), divide the image into four equal regions and apply fixed-level color reduction on each region, using different numbers of color levels for each region (e.g., 2, 4, 8, and 16 levels). Save the final image as "color_reduction.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def divide_image(image:np.ndarray, rows:int, cols:int) -> np.ndarray:
    regions = []
    for i in range(rows):
        for j in range(cols):
            x = i * image.shape[0] // rows
            y = j * image.shape[1] // cols
            w = image.shape[0] // rows
            h = image.shape[1] // cols
            regions.append(image[x:x+w, y:y+h])
    return regions

def color_reduction(image:np.ndarray, levels:int) -> np.ndarray:
    return (image // (256 // levels)) * (256 // levels)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # divide the image into four regions
    regions = divide_image(image, 2, 2)
    
    # apply fixed-level color reduction
    levels = [2, 4, 8, 16]
    for i, level in enumerate(levels):
        regions[i] = color_reduction(regions[i], level)
    
    # merge the regions
    result = np.vstack([np.hstack(regions[:2]), np.hstack(regions[2:])])
    
    cv2.imwrite('color_reduction.png', result)

def test():
    assert Path('color_reduction.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('color_reduction.png')
    
    # divide the image into four regions
    regions = divide_image(image, 2, 2)
    
    # apply fixed-level color reduction
    levels = [2, 4, 8, 16]
    for i, level in enumerate(levels):
        regions[i] = color_reduction(regions[i], level)
    
    # merge the regions
    result_test = np.vstack([np.hstack(regions[:2]), np.hstack(regions[2:])])
    
    # assert that the images are the same
    assert np.array_equal(result, result_test)

    # clean up
    # os.remove('color_reduction.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')