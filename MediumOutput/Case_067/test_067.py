'''
Given an image ("./test_image.png"), detect corners (use maxCorners=100, qualityLevel=0.01, minDistance=10) and draw it in red (radius=3, thickness = -1), rotate at 90-degree, detect and draw corners again then rotate back to the original orientation and save the original and rotated back images as "original_image.png" and "rotated_image_back.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def detect_corners(image:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    return np.int0(corners)

def draw_corners(image:np.ndarray, corners:np.ndarray) -> np.ndarray:
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
    return image

def rotate_image(image:np.ndarray, angle:int) -> np.ndarray:
    h, w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # detect corners
    corners = detect_corners(image)
    image = draw_corners(image, corners)
    cv2.imwrite('original_image.png', image)

    # rotate at 90-degree
    rotated_image = rotate_image(image, 90)

    # detect corners again
    corners_rotated = detect_corners(rotated_image)
    rotated_image = draw_corners(rotated_image, corners_rotated)

    # rotrate the image back to the original orientation
    rotated_image = rotate_image(rotated_image, -90)
    cv2.imwrite('rotated_image_back.png', rotated_image)

def test():
    assert Path('original_image.png').exists()
    assert Path('rotated_image_back.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    original_image = cv2.imread('original_image.png')
    rotated_image_back = cv2.imread('rotated_image_back.png')
    
    # detect corners
    corners = detect_corners(image)
    original_image_new = draw_corners(original_image, corners)
    
    # rotate at 90-degree
    rotated_image = rotate_image(original_image, 90)
    
    # detect corners again
    corners_rotated = detect_corners(rotated_image)
    rotated_image = draw_corners(rotated_image, corners_rotated)
    
    # rotrate the image back to the original orientation
    rotated_image = rotate_image(rotated_image, -90)
    
    # assert that the images are the same
    assert np.array_equal(original_image, original_image_new)
    assert np.array_equal(rotated_image, rotated_image_back)

    # clean up
    # os.remove('original_image.png')
    # os.remove('rotated_image_back.png')

if __name__ == "__main__":
    # main()
    test()
    print('All tests passed')
