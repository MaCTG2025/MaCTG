'''
Given an RGB image ("./test_image.png"), slpit it into three separate images, one for each channel (R, G, B) and save them as separate png files: "red_channel.png", "green_channel.png" and "blue_channel.png".
'''
import cv2
from PIL import Image
import numpy as np
from pathlib import Path
import os

def split_channels(image_path:Path):
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    cv2.imwrite('red_channel.png', r)
    cv2.imwrite('green_channel.png', g)
    cv2.imwrite('blue_channel.png', b)

def main():
    image_path = Path('./test_image.png')
    split_channels(image_path)

def test():
    assert Path('red_channel.png').exists()
    assert Path('green_channel.png').exists()
    assert Path('blue_channel.png').exists()

    # load the original image
    original = Image.open('test_image.png')
    original_array = np.array(original)

    # check red channel
    R = Image.open('red_channel.png')
    R_array = np.array(R)
    assert np.array_equal(R_array, original_array[:,:,0])

    # check green channel
    G = Image.open('green_channel.png')
    G_array = np.array(G)
    assert np.array_equal(G_array, original_array[:,:,1])

    # check blue channel
    B = Image.open('blue_channel.png')
    B_array = np.array(B)
    assert np.array_equal(B_array, original_array[:,:,2])

    # clean up
    # os.remove('red_channel.png')
    # os.remove('green_channel.png')
    # os.remove('blue_channel.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')