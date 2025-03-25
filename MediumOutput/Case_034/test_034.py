'''
Given an image ("./test_image.png"), apply a circular mask (radius = 100 pixels) and a Gaussian blur (kernel size = 15, sigmaX = 10) outside the mask, keeping the center of the image sharp. Save the resulting image as "final_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def mask_center(image:np.ndarray, mask_size:int) -> np.ndarray:
    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    center = (w//2, h//2)
    cv2.circle(mask, center, mask_size, 255, -1)
    return mask

def apply_gaussian_blur(image:np.ndarray, kernel_size:int, sigmaX:float) -> np.ndarray:
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    mask = mask_center(image, 100)
    blurred_image = apply_gaussian_blur(image, 15, 10)
    blurred_image[np.where(mask == 255)] = image[np.where(mask == 255)]
    cv2.imwrite('final_image.png', blurred_image)

def test():
    assert Path('final_image.png').exists()

    image = load_image(Path('./test_image.png'))
    mask = mask_center(image, 100)
    blurred_image = apply_gaussian_blur(image, 15, 10)
    blurred_image[np.where(mask == 255)] = image[np.where(mask == 255)]
    result = cv2.imread('final_image.png')
    assert np.array_equal(blurred_image, result)

    # clean up
    # os.remove('final_image.png')

if __name__ == '__main__':
    main()
    test()
    print('All tests passed')