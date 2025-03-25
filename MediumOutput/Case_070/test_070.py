'''
Given an image ("./test_image.png"), split into R, G, B channels, apply keypoint matching (ORB) to each channel, draw keypoints in red and save the results as "keypoints_R.png", "keypoints_G.png", and "keypoints_B.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def split_channels(image:np.ndarray) -> np.ndarray:
    return cv2.split(image)

def detect_keypoints(image:np.ndarray) -> np.ndarray:
    orb = cv2.ORB_create()
    keypoints = orb.detect(image, None)
    return keypoints

def draw_keypoints(image:np.ndarray, keypoints:np.ndarray) -> np.ndarray:
    return cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # split the image into R, G, B channels
    channels = split_channels(image)
    
    # detect keypoints in each channel
    keypoints_R = detect_keypoints(channels[0])
    keypoints_G = detect_keypoints(channels[1])
    keypoints_B = detect_keypoints(channels[2])
    
    # draw the keypoints
    keypoints_R = draw_keypoints(channels[0], keypoints_R)
    keypoints_G = draw_keypoints(channels[1], keypoints_G)
    keypoints_B = draw_keypoints(channels[2], keypoints_B)
    
    cv2.imwrite('keypoints_R.png', keypoints_R)
    cv2.imwrite('keypoints_G.png', keypoints_G)
    cv2.imwrite('keypoints_B.png', keypoints_B)

def test():
    assert Path('keypoints_R.png').exists()
    assert Path('keypoints_G.png').exists()
    assert Path('keypoints_B.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    keypoints_R = cv2.imread('keypoints_R.png')
    keypoints_G = cv2.imread('keypoints_G.png')
    keypoints_B = cv2.imread('keypoints_B.png')
    
    # split the image into R, G, B channels
    channels = cv2.split(image)
    
    # detect keypoints in each channel
    keypoints_R_test = detect_keypoints(channels[0])
    keypoints_G_test = detect_keypoints(channels[1])
    keypoints_B_test = detect_keypoints(channels[2])
    
    # draw the keypoints
    keypoints_R_test = draw_keypoints(channels[0], keypoints_R_test)
    keypoints_G_test = draw_keypoints(channels[1], keypoints_G_test)
    keypoints_B_test = draw_keypoints(channels[2], keypoints_B_test)
    
    # assert that the images are the same
    assert np.array_equal(keypoints_R, keypoints_R_test)
    assert np.array_equal(keypoints_G, keypoints_G_test)
    assert np.array_equal(keypoints_B, keypoints_B_test)

    # clean up
    # os.remove('keypoints_R.png')
    # os.remove('keypoints_G.png')
    # os.remove('keypoints_B.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')

