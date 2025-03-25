'''
Given a list of images taken at different exposure levels ("./hdr_1.png"), ("./hdr_2.png"), ("./hdr_3.png"), the exposure time for each image is [1/2, 1/0.5, 1/0.0625], develop an algorithm to merge them into a single HDR image, save the output image as "./hdr_image.hdr".
'''


import cv2
import numpy as np
import os
from typing import List


def load_image(image_path: str) -> np.ndarray:
    return cv2.imread(image_path)

def compute_crf(images: List[np.ndarray], exposure_times: np.ndarray) -> np.ndarray:
    calibrate = cv2.createCalibrateDebevec()
    response_debevec = calibrate.process(images, exposure_times)
    return response_debevec

def merge_hdr(images: List[np.ndarray], exposure_times: np.ndarray, response_debevec: np.ndarray) -> np.ndarray:
    merge = cv2.createMergeDebevec()
    hdr = merge.process(images, exposure_times, response_debevec)
    return hdr

def save_hdr(hdr: np.ndarray, output_path: str) -> None:
    cv2.imwrite(output_path, hdr)

def main():
    images = [load_image(f"./hdr_{i}.png") for i in range(1, 4)]
    exposure_times = np.array([1/2, 1/0.5, 1/0.0625], dtype=np.float32)
    response_debevec = compute_crf(images, exposure_times)
    hdr = merge_hdr(images, exposure_times, response_debevec)
    save_hdr(hdr, "./hdr_image.hdr")

def test():
    assert os.path.exists("./hdr_image.hdr")

    result = cv2.imread("./hdr_image.hdr", cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

    images = [load_image(f"./hdr_{i}.png") for i in range(1, 4)]
    exposure_times = np.array([1/2, 1/0.5, 1/0.0625], dtype=np.float32)
    response_debevec = compute_crf(images, exposure_times)
    hdr = merge_hdr(images, exposure_times, response_debevec)

    assert np.allclose(hdr, result, atol=1)

    # clean up
    # os.remove("./hdr_image.hdr")

if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")
