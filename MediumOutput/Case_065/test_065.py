'''
Given an image ("./test_image.png"), convert to HSV, apply a circle mask at the center of the Hue channel with a radius of 100 pixels, convert it back to RGB and save the masked image as "masked_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_hsv(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def split_channels(image:np.ndarray) -> np.ndarray:
    return cv2.split(image)

def convert_to_rgb(image:np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

def apply_circle_mask(image:np.ndarray, center:tuple, radius:int) -> np.ndarray:
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, center, radius, 255, -1)
    image = cv2.bitwise_and(image, mask)
    return image

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # convert to HSV
    hsv_image = convert_to_hsv(image)
    h, s, v = split_channels(hsv_image)
    
    # apply a circle mask at the center of the Hue channel
    center = (image.shape[1]//2, image.shape[0]//2)
    radius = 100
    h = apply_circle_mask(h, center, radius)

    # convert it back to RGB
    masked_image = convert_to_rgb(cv2.merge([h, s, v]))

    # save the masked image
    cv2.imwrite('masked_image.png', masked_image)

def test():
    assert Path('masked_image.png').exists()
    
    # load the image
    image = cv2.imread('test_image.png')
    
    # convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    
    # apply a circle mask at the center of the Hue channel
    center = (image.shape[1]//2, image.shape[0]//2)
    radius = 100
    h = apply_circle_mask(h, center, radius)
    
    # convert it back to RGB
    masked_image = cv2.cvtColor(cv2.merge([h, s, v]), cv2.COLOR_HSV2BGR)
    
    # load the masked image
    masked_image_test = cv2.imread('masked_image.png')
    
    # assert that the images are the same
    assert np.array_equal(masked_image, masked_image_test)

    # clean up
    # os.remove('masked_image.png')

if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")
