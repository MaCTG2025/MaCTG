'''
Given two images, one background image ("./abraham.jpg") and one object image ("./test_image.png"), first applying a 0.5x downscale then rotate 45 degrees to the object, then placing the transformed object onto the center of background using seamless cloning (Poisson blending). Save the result as "seamless_cloning.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def downscale_image(image:np.ndarray, scale:float) -> np.ndarray:
    return cv2.resize(image, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

def rotate_image(image:np.ndarray, angle:float) -> np.ndarray:
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def seamless_cloning(background:np.ndarray, object:np.ndarray) -> np.ndarray:
    mask = 255 * np.ones(object.shape, object.dtype)
    center = (background.shape[1]//2, background.shape[0]//2)
    return cv2.seamlessClone(object, background, mask, center, cv2.NORMAL_CLONE)

def main():
    background_path = Path('./abraham.jpg')
    object_path = Path('./test_image.png')
    background = load_image(background_path)
    object = load_image(object_path)
    
    # downscale the object
    object = downscale_image(object, 0.5)
    
    # rotate the object
    object = rotate_image(object, 45)
    
    # seamless cloning
    result = seamless_cloning(background, object)
    
    cv2.imwrite('seamless_cloning.png', result)

def test():
    assert Path('seamless_cloning.png').exists()
    
    # load the images
    background = cv2.imread('abraham.jpg')
    object = cv2.imread('test_image.png')
    result = cv2.imread('seamless_cloning.png')
    
    # downscale the object
    object = downscale_image(object, 0.5)
    
    # rotate the object
    object = rotate_image(object, 45)
    
    # seamless cloning
    result_test = seamless_cloning(background, object)
    
    # assert that the images are the same
    assert np.array_equal(result, result_test)

    # clean up
    # os.remove('seamless_cloning.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')