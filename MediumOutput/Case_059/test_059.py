'''
Given an image ("./seg_image.png"), apply K-means clustering to segment the image into distinct color regions based on pixel values. Use a specified number of clusters (e.g., k = 4), assign each pixel to its corresponding cluster, and save the segmented image with each region color-coded as "seg_image_kmeans.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path)
    return image

def apply_kmeans_clustering(image:np.ndarray, k:int)->np.ndarray:
    Z = image.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.1)
    ret,label,center=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((image.shape))

def main()->None:
    image_path = Path('./seg_image.png')
    image = load_image(image_path)
    result = apply_kmeans_clustering(image, 4)
    cv2.imwrite('seg_image_kmeans.png', result)

def test():
    result = cv2.imread('seg_image_kmeans.png')

    image_path = Path('./seg_image.png')
    image = load_image(image_path)
    expected = apply_kmeans_clustering(image, 4)

    assert np.allclose(result, expected)

    # cleanup
    # os.remove('seg_image_kmeans.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")