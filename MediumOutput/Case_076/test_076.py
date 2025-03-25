'''
Given an image ("./test_image.png"), divide the image into equal-sized tiles (2x2 grid of tiles), apply rotation (0°, 90°, 180°, and 270°) to each tile, and then reassemble the tiles back into a mosaic-style image. Save the final mosaic image as "rotated_tiles.png".
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

def rotate_image(image:np.ndarray, angle:float) -> np.ndarray:
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # divide the image into four regions
    regions = divide_image(image, 2, 2)
    
    # apply rotation to each region
    angles = [0, 90, 180, 270]
    for i, angle in enumerate(angles):
        regions[i] = rotate_image(regions[i], angle)
    
    # merge the regions
    result = np.vstack([np.hstack(regions[:2]), np.hstack(regions[2:])])
    
    cv2.imwrite('rotated_tiles.png', result)


def test():
    assert Path('rotated_tiles.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('rotated_tiles.png')
    
    # divide the image into four regions
    regions = divide_image(image, 2, 2)
    
    # apply rotation to each region
    angles = [0, 90, 180, 270]
    for i, angle in enumerate(angles):
        regions[i] = rotate_image(regions[i], angle)
    
    # merge the regions
    result_test = np.vstack([np.hstack(regions[:2]), np.hstack(regions[2:])])
    
    # assert that the images are the same
    assert np.array_equal(result, result_test)

    #cleanup
    # os.remove('rotated_tiles.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')