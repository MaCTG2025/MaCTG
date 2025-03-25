'''
Given an image ("./test_image.png"), apply arithmetic addition operations to the central circle region (radius=100) and subtraction operations to the outer region. The addition and subtraction values are 50 and 100, respectively. Save the resulting image as "final_image.png".
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

def apply_arithmetic_operations(image:np.ndarray, mask:np.ndarray, add_value:int, subtract_value:int) -> np.ndarray:
    result = np.zeros_like(image)
    result[np.where(mask == 255)] = cv2.add(image, add_value)[np.where(mask == 255)]
    result[np.where(mask == 0)] = cv2.subtract(image, subtract_value)[np.where(mask == 0)]
    return np.clip(result, 0, 255).astype(np.uint8)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    mask = mask_center(image, 100)
    final_image = apply_arithmetic_operations(image, mask, 50, 100)
    cv2.imwrite('final_image.png', final_image)

def test():
    assert Path('final_image.png').exists()

    image = load_image(Path('./test_image.png'))
    mask = mask_center(image, 100)
    final_image = apply_arithmetic_operations(image, mask, 50, 100)
    result = cv2.imread('final_image.png')
    assert np.array_equal(final_image, result)

    # clean up
    # os.remove('final_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')