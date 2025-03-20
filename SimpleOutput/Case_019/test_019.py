'''
Given an input image ("./test_image.png"), first convert it into HSV color space. Then, split the image into its three channels (Hue, Saturation, Value). Finally, save the HSV image as "HSV.png" and the three channels as "hue_channel.png", "saturation_channel.png", and "value_channel.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def convert_to_hsv(image:np.ndarray)->np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def split_channels(image:np.ndarray)->np.ndarray:
    return cv2.split(image)

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path_hsv = Path("./HSV.png")
    save_path_hue = Path("./hue_channel.png")
    save_path_saturation = Path("./saturation_channel.png")
    save_path_value = Path("./value_channel.png")

    image = load_image(image_path)
    hsv_image = convert_to_hsv(image)
    hue, saturation, value = split_channels(hsv_image)
    save_image(hsv_image, save_path_hsv)
    save_image(hue, save_path_hue)
    save_image(saturation, save_path_saturation)
    save_image(value, save_path_value)

def test():
    save_path_hsv = Path("./HSV.png")
    save_path_hue = Path("./hue_channel.png")
    save_path_saturation = Path("./saturation_channel.png")
    save_path_value = Path("./value_channel.png")
    assert save_path_hsv.exists(), f"{save_path_hsv} does not exist"
    assert save_path_hue.exists(), f"{save_path_hue} does not exist"
    assert save_path_saturation.exists(), f"{save_path_saturation} does not exist"
    assert save_path_value.exists(), f"{save_path_value} does not exist"
    input_image = cv2.imread("./test_image.png")
    hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(hsv_image)
    result_hsv = cv2.imread("./HSV.png")
    result_hue = cv2.imread("./hue_channel.png", cv2.IMREAD_GRAYSCALE)
    result_saturation = cv2.imread("./saturation_channel.png", cv2.IMREAD_GRAYSCALE)
    result_value = cv2.imread("./value_channel.png", cv2.IMREAD_GRAYSCALE)
    assert np.array_equal(result_hsv, hsv_image), f"Expected {result_hsv} but got {hsv_image}"
    assert np.array_equal(result_hue, hue), f"Expected {result_hue} but got {hue}"
    assert np.array_equal(result_saturation, saturation), f"Expected {result_saturation} but got {saturation}"
    assert np.array_equal(result_value, value), f"Expected {result_value} but got {value}"
    # cleanup
    # os.remove(save_path_hsv)
    # os.remove(save_path_hue)
    # os.remove(save_path_saturation)
    # os.remove(save_path_value)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')