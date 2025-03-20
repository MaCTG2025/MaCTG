'''
Given an RGB image ("./test_image.png"), slpit it into R, G, and B channels. For each channel, save it as RGB image with the channel as the only non-zero channel. For example, the red channel image should have the red channel as the only non-zero channel, and the green and blue channels should be zero. Save the three images as "red_channel.png", "green_channel.png" and "blue_channel.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(image_path)

def split_channels_and_restore(image:np.ndarray) -> np.ndarray:
    b, g, r = cv2.split(image)
    zeros = np.zeros_like(b)
    red = cv2.merge((zeros, zeros, r))
    green = cv2.merge((zeros, g, zeros))
    blue = cv2.merge((b, zeros, zeros))
    return red, green, blue

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./test_image.png')
    image = load_image(str(image_path))
    red, green, blue = split_channels_and_restore(image)
    save_image(red, Path('./red_channel.png'))
    save_image(green, Path('./green_channel.png'))
    save_image(blue, Path('./blue_channel.png'))

def test():
    assert Path('red_channel.png').exists()
    assert Path('green_channel.png').exists()
    assert Path('blue_channel.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    red, green, blue = split_channels_and_restore(original)

    # load the image with corners
    red_result = cv2.imread('red_channel.png')
    green_result = cv2.imread('green_channel.png')
    blue_result = cv2.imread('blue_channel.png')

    assert np.array_equal(red, red_result)
    assert np.array_equal(green, green_result)
    assert np.array_equal(blue, blue_result)

    # clean up
    # os.remove('red_channel.png')
    # os.remove('green_channel.png')
    # os.remove('blue_channel.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')