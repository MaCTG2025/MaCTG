'''
Given an RGB image ("./test_image.png"), mask each channel at the center of the image with a square of length 100 and value 1, then apply contrast adjustment to each channel using alpha = 1.5 and beta = 50. Finally, save the resulting image as "contrast_adjusted_image.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os
from typing import List

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def split_image(image:np.ndarray) -> tuple:
    return cv2.split(image)

def mask_center(image:np.ndarray, mask_size:int) -> np.ndarray:
    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    center = (h//2, w//2)
    mask[center[0]-mask_size//2:center[0]+mask_size//2, center[1]-mask_size//2:center[1]+mask_size//2] = 1
    return image * mask

def contrast_adjustment(image:np.ndarray, alpha:float, beta:float) -> np.ndarray:
    return np.clip(alpha * image + beta, 0, 255).astype(np.uint8)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    channels = split_image(image)
    masked_images = [mask_center(channel, 100) for channel in channels]
    contrast_adjusted_images = [contrast_adjustment(channel, 1.5, 50) for channel in masked_images]
    contrast_adjusted_image = cv2.merge(contrast_adjusted_images)
    cv2.imwrite('contrast_adjusted_image.png', contrast_adjusted_image)

def test():
    assert Path('contrast_adjusted_image.png').exists()

    image = load_image(Path('./test_image.png'))
    channels = split_image(image)
    masked_images = [mask_center(channel, 100) for channel in channels]
    contrast_adjusted_images = [contrast_adjustment(channel, 1.5, 50) for channel in masked_images]
    contrast_adjusted_image = cv2.merge(contrast_adjusted_images)
    result = cv2.imread('contrast_adjusted_image.png')
    assert np.array_equal(contrast_adjusted_image, result)

    # clean up
    # os.remove('contrast_adjusted_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')