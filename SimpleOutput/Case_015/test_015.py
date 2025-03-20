'''
Given an input image ("./test_image.png"), apply a arithmetic add and a substraction operation to it. The adding/subtraction parameter is a value of 100. Save the resulting images as "added_image.png" and "subtracted_image.png".
'''

import cv2
from PIL import Image
from pathlib import Path
import os
import numpy as np
from typing import Tuple

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def add_subtract_image(image:np.ndarray, value:int)->Tuple[np.ndarray, np.ndarray]:
    added_image = cv2.add(image, value)
    subtracted_image = cv2.subtract(image, value)
    return added_image, subtracted_image

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path_add = Path("./added_image.png")
    save_path_sub = Path("./subtracted_image.png")
    value = 100

    image = load_image(image_path)
    added_image, subtracted_image = add_subtract_image(image, value)
    save_image(added_image, save_path_add)
    save_image(subtracted_image, save_path_sub)

def test():
    save_path_add = Path("./added_image.png")
    save_path_sub = Path("./subtracted_image.png")
    assert save_path_add.exists(), f"{save_path_add} does not exist"
    assert save_path_sub.exists(), f"{save_path_sub} does not exist"
    input_image = cv2.imread("./test_image.png")
    result_add = cv2.imread("./added_image.png")
    result_sub = cv2.imread("./subtracted_image.png")
    value = 100
    output_add, output_sub = add_subtract_image(input_image, value)
    assert np.array_equal(result_add, output_add), f"Expected {result_add} but got {output_add}"
    assert np.array_equal(result_sub, output_sub), f"Expected {result_sub} but got {output_sub}"
    # cleanup
    # os.remove(save_path_add)
    # os.remove(save_path_sub)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')