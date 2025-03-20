'''
Given an input image ("./test_image.png"), perform a 180 degree rotation then a vertical flip on it. Save the resulting image as "rotated_flipped_image.png".
'''

import cv2
from pathlib import Path
import os
import numpy as np

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def rotate_flip_image(image:np.ndarray)->np.ndarray:
    image = cv2.rotate(image, cv2.ROTATE_180)
    return cv2.flip(image, 0)

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path = Path("./rotated_flipped_image.png")

    image = load_image(image_path)
    image = rotate_flip_image(image)
    save_image(image, save_path)

def test():
    save_path = Path("./rotated_flipped_image.png")
    assert save_path.exists(), f"{save_path} does not exist"
    input_image = cv2.imread("./test_image.png")
    result = cv2.imread("./rotated_flipped_image.png")
    output_image = cv2.flip(cv2.rotate(input_image, cv2.ROTATE_180), 0)
    assert np.array_equal(result, output_image), f"Expected {result} but got {output_image}"
    # cleanup
    # os.remove(save_path)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')