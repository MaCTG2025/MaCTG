'''
Given an input image ("./test_image.png"), add a mask to it. The mask is a white circle with a radius of 100 pixels centered at the center of the image with the rest pixels in black. Save the resulting image as "masked_image.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def add_mask(image:np.ndarray)->np.ndarray:
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, (image.shape[1]//2, image.shape[0]//2), 100, 255, -1)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    return masked_image

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    masked_image = add_mask(image)
    save_image(masked_image, Path('./masked_image.png'))

def test():
    assert Path('masked_image.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    masked = add_mask(original)

    # load the image with corners
    masked_result = cv2.imread('masked_image.png')

    assert np.array_equal(masked, masked_result)

    # clean up
    # os.remove('masked_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')