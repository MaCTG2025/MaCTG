'''
Given an input image ("./test_image.png"), do 2 pyramid scalings on it, one upscaling and one downscaling. Save the resulting images as "upscaled.png" and "downscaled.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def upscale(image:np.ndarray)->np.ndarray:
    return cv2.pyrUp(image)

def downscale(image:np.ndarray)->np.ndarray:
    return cv2.pyrDown(image)

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    upscaled = upscale(image)
    downscaled = downscale(image)
    save_image(upscaled, Path('./upscaled.png'))
    save_image(downscaled, Path('./downscaled.png'))

def test():
    assert Path('upscaled.png').exists()
    assert Path('downscaled.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    upscaled = upscale(original)
    downscaled = downscale(original)

    # load the image with corners
    upscaled_result = cv2.imread('upscaled.png')
    downscaled_result = cv2.imread('downscaled.png')

    assert np.array_equal(upscaled, upscaled_result)
    assert np.array_equal(downscaled, downscaled_result)

    # clean up
    # os.remove('upscaled.png')
    # os.remove('downscaled.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')