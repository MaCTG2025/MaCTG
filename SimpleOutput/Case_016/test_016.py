'''
Given an input image ("./test_image.png"), crop the middle 75% of the image and save it as "cropped_image.png".
'''

import cv2
from PIL import Image
from pathlib import Path
import os
import numpy as np

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def crop_image(image:np.ndarray)->np.ndarray:
    h, w = image.shape[:2]
    start_h = h//8
    start_w = w//8
    end_h = h - start_h
    end_w = w - start_w
    return image[start_h:end_h, start_w:end_w]

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path = Path("./cropped_image.png")

    image = load_image(image_path)
    image = crop_image(image)
    save_image(image, save_path)

def test():
    save_path = Path("./cropped_image.png")
    assert save_path.exists(), f"{save_path} does not exist"
    input_image = cv2.imread("./test_image.png")
    h, w = input_image.shape[:2]
    start_h = h//8
    start_w = w//8
    end_h = h - start_h
    end_w = w - start_w
    output_image = input_image[start_h:end_h, start_w:end_w]
    result = cv2.imread("./cropped_image.png")
    assert np.array_equal(result, output_image), f"Expected {result} but got {output_image}"
    # cleanup
    # os.remove(save_path)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')