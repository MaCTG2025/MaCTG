'''
Given an input image ("./test_image.png"), rescale the image into twice its original size using Linear Interpolation, Cubic Interpolation and Area Interpolation. Save the resulting images as \"linear_interpolation.png\", \"cubic_interpolation.png\" and \"area_interpolation.png
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def rescale_image(image:np.ndarray, scale:float, interpolation:int)->np.ndarray:
    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=interpolation)

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path_linear = Path("./linear_interpolation.png")
    save_path_cubic = Path("./cubic_interpolation.png")
    save_path_area = Path("./area_interpolation.png")
    scale = 2

    image = load_image(image_path)
    linear_image = rescale_image(image, scale, cv2.INTER_LINEAR)
    cubic_image = rescale_image(image, scale, cv2.INTER_CUBIC)
    area_image = rescale_image(image, scale, cv2.INTER_AREA)
    save_image(linear_image, save_path_linear)
    save_image(cubic_image, save_path_cubic)
    save_image(area_image, save_path_area)

def test():
    save_path_linear = Path("./linear_interpolation.png")
    save_path_cubic = Path("./cubic_interpolation.png")
    save_path_area = Path("./area_interpolation.png")
    assert save_path_linear.exists(), f"{save_path_linear} does not exist"
    assert save_path_cubic.exists(), f"{save_path_cubic} does not exist"
    assert save_path_area.exists(), f"{save_path_area} does not exist"
    input_image = cv2.imread("./test_image.png")
    result_linear = cv2.imread("./linear_interpolation.png")
    result_cubic = cv2.imread("./cubic_interpolation.png")
    result_area = cv2.imread("./area_interpolation.png")
    scale = 2
    output_linear = cv2.resize(input_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    output_cubic = cv2.resize(input_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    output_area = cv2.resize(input_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    assert np.array_equal(result_linear, output_linear), f"Expected {result_linear} but got {output_linear}"
    assert np.array_equal(result_cubic, output_cubic), f"Expected {result_cubic} but got {output_cubic}"
    assert np.array_equal(result_area, output_area), f"Expected {result_area} but got {output_area}"
    # cleanup
    # os.remove(save_path_linear)
    # os.remove(save_path_cubic)
    # os.remove(save_path_area)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')