'''
Given an image ("./blobs.jpg"), detect blobs, filter them by area (minArea = 1500, maxArea = 5000), draw the filtered blobs, and save the result as "filtered_blobs.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def detect_blobs(image:np.ndarray) -> np.ndarray:
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 1500
    params.maxArea = 5000
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)
    return keypoints

def draw_blobs(image:np.ndarray, keypoints:np.ndarray) -> np.ndarray:
    return cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)   

def main():
    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    
    # detect blobs
    keypoints = detect_blobs(image)
    
    # draw the filtered blobs
    image = draw_blobs(image, keypoints)
    cv2.imwrite('filtered_blobs.png', image)

def test():
    assert Path('filtered_blobs.png').exists()
    
    # load the images
    image = cv2.imread('blobs.jpg')
    filtered_blobs = cv2.imread('filtered_blobs.png')
    
    # detect blobs
    keypoints = detect_blobs(image)
    
    # draw the filtered blobs
    filtered_blobs_test = draw_blobs(image, keypoints)
    
    # assert that the images are the same
    assert np.array_equal(filtered_blobs, filtered_blobs_test)

    # clean up
    # os.remove('filtered_blobs.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')