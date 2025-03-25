'''
Given an image ("./blobs.jpg"), detect all blobs and change the blobs into red (R=255, G=0, B=0) to the blob regions, then save the resulting image as "blobs_red.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path):
    return cv2.imread(str(image_path))

def binarize_image(image:np.ndarray):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    return thresh

def detect_blobs(bin_image:np.ndarray):
    detector = cv2.SimpleBlobDetector_create()
    keypoints = detector.detect(bin_image)

    return keypoints

def change_blob_color(bin_image:np.ndarray, image:np.ndarray, keypoints):
    h, w  = bin_image.shape
    for keypoint in keypoints:
        x, y = keypoint.pt
        s = keypoint.size

        boundry = [max(0, int(x-s)), min(w, int(x+s)), max(0, int(y-s)), min(h, int(y+s))]
        image[boundry[2]:boundry[3], boundry[0]:boundry[1]][np.where(bin_image[boundry[2]:boundry[3], boundry[0]:boundry[1]] == 0)] = [0, 0, 255]
    
    return image


def main():
    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    bin_image = binarize_image(image)
    keypoints = detect_blobs(bin_image)
    image = change_blob_color(bin_image, image, keypoints)

    cv2.imwrite('./blobs_red.png', image)

def test():
    assert Path('./blobs_red.jpg').exists()

    result = cv2.imread('./blobs_red.png')
    image = load_image(Path('./blobs.jpg'))
    bin_image = binarize_image(image)
    keypoints = detect_blobs(bin_image)
    image = change_blob_color(bin_image, image, keypoints)

    assert np.array_equal(image, result)

    # clean up
    # os.remove('./blobs_red.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')