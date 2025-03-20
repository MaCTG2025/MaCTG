'''
Given an input image ("./test_image.png"), perform fast mean denoising on it. Use the following parameters: h=11, hForColorComponents=6, templateWindowSize=7, searchWindowSize=21. Save the resulting image as "denoised_image.png".
'''

import cv2
from PIL import Image
from pathlib import Path
import os
import numpy as np

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def denoise_image(image:np.ndarray, h:int, hForColorComponents:int, templateWindowSize:int, searchWindowSize:int)->np.ndarray:
    return cv2.fastNlMeansDenoisingColored(image, None, h, hForColorComponents, templateWindowSize, searchWindowSize)

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path = Path("./denoised_image.png")
    h = 11
    hForColorComponents = 6
    templateWindowSize = 7
    searchWindowSize = 21

    image = load_image(image_path)
    image = denoise_image(image, h, hForColorComponents, templateWindowSize, searchWindowSize)
    save_image(image, save_path)

def test():
    save_path = Path("./denoised_image.png")
    assert save_path.exists(), f"{save_path} does not exist"
    input_image = cv2.imread("./test_image.png")
    result = cv2.imread("./denoised_image.png")
    h = 11
    hForColorComponents = 6
    templateWindowSize = 7
    searchWindowSize = 21
    output_image = cv2.fastNlMeansDenoisingColored(input_image, None, h, hForColorComponents, templateWindowSize, searchWindowSize)
    assert np.array_equal(result, output_image), f"Expected {result} but got {output_image}"
    # cleanup
    # os.remove(save_path)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')