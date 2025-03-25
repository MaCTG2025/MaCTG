'''
Given an image ("./blobs.jpg"), detect blobs using SimpleBlobDetector, classify them by circularity (threshold=0.7), inertia (threshold=0.5), convexity (threshold=0.9), and save the image with highlighted blobs as "blobs_image.png".
'''

import cv2
from pathlib import Path
import os
import numpy as np

def find_blobs(image_path:Path) -> np.ndarray:
    image = cv2.imread(str(image_path))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binarized_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    
    params = cv2.SimpleBlobDetector_Params()

    params.filterByCircularity = True
    params.minCircularity = 0.7

    params.filterByInertia = True
    params.minInertiaRatio = 0.5

    params.filterByConvexity = True
    params.minConvexity = 0.9

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(binarized_image)

    image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    return image

def main():
    image_path = Path('./blobs.jpg')
    image = find_blobs(image_path)
    cv2.imwrite('blobs_image.png', image)

def test():
    assert Path('blobs_image.png').exists()

    # load the blobs image
    result = cv2.imread('blobs_image.png')
    image = find_blobs(Path('./blobs.jpg'))

    assert np.array_equal(image, result)

    # clean up
    # os.remove('blobs_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')