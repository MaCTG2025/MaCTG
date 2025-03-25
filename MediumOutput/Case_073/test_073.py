'''
Given an image ("./blobs.jpg"), apply a circular mask at the center of the image with a radius of 100 pixels, and detect blobs only within the masked region. Draw the detected blobs (using drawKeypoints) and save the result as "masked_blobs.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def create_circular_mask(image:np.ndarray, center:tuple, radius:int) -> np.ndarray:
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, center, radius, 255, -1)
    return mask

def detect_blobs(image:np.ndarray, mask:np.ndarray) -> np.ndarray:
    params = cv2.SimpleBlobDetector_Params()
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image, mask)
    return keypoints

def draw_blobs(image:np.ndarray, keypoints:np.ndarray) -> np.ndarray:
    return cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

def main():
    image_path = Path('./blobs.jpg')
    image = load_image(image_path)
    
    # create a circular mask
    center = (image.shape[1]//2, image.shape[0]//2)
    mask = create_circular_mask(image, center, 100)
    
    # detect blobs within the masked region
    keypoints = detect_blobs(image, mask)
    
    # draw the detected blobs
    image = draw_blobs(image, keypoints)
    cv2.imwrite('masked_blobs.png', image)

def test():
    assert Path('masked_blobs.png').exists()
    
    # load the images
    image = cv2.imread('blobs.jpg')
    masked_blobs = cv2.imread('masked_blobs.png')
    
    # create a circular mask
    center = (image.shape[1]//2, image.shape[0]//2)
    mask = create_circular_mask(image, center, 100)
    
    # detect blobs within the masked region
    keypoints = detect_blobs(image, mask)
    
    # draw the detected blobs
    masked_blobs_test = draw_blobs(image, keypoints)
    
    # assert that the images are the same
    assert np.array_equal(masked_blobs, masked_blobs_test)

    # clean up
    # os.remove('masked_blobs.png')   

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')