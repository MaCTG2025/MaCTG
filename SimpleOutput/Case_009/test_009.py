'''
Given an input image ("./blobs.jpg"), find the blobs in the image. Draw the bounding boxes of the blobs in red (using drawKeypoints) and save the resulting image as "blobs_image.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def find_blobs(image:np.ndarray)->np.ndarray:
    detector = cv2.SimpleBlobDetector_create()
    keypoints = detector.detect(image)
    return cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    blobs_image = find_blobs(image)
    save_image(blobs_image, Path('./blobs_image.png'))

def test():
    assert Path('blobs_image.png').exists()

    # load the original image
    original = cv2.imread('blobs.jpg')

    blobs = find_blobs(original)

    # load the image with corners
    blobs_result = cv2.imread('blobs_image.png')

    assert np.array_equal(blobs, blobs_result)

    # clean up
    # os.remove('blobs_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')