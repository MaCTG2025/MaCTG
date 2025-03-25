'''
Given an image ("./blobs.jpg"), detect blobs, for each blob, compute the center, area and perimeter, save the result into "blobs.npy".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

def detect_blobs(image:np.ndarray)->np.ndarray:
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 100
    params.filterByCircularity = True
    params.minCircularity = 0.8
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)
    return keypoints

def compute_properties(keypoints:np.ndarray)->np.ndarray:
    properties = []
    for keypoint in keypoints:
        x, y = keypoint.pt
        area = keypoint.size
        perimeter = keypoint.size * np.pi
        properties.append((x, y, area, perimeter))
    return np.array(properties)

def main()->None:
    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    keypoints = detect_blobs(image)
    properties = compute_properties(keypoints)
    np.save('blobs.npy', properties)

def test():
    result = np.load('blobs.npy')

    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    keypoints = detect_blobs(image)
    expected = compute_properties(keypoints)

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('blobs.npy')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")