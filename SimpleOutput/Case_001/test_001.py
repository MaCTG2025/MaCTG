'''
Given an input image ("./squares.jpg"), find all corners of the squares in the image and draw them as red circles(radius=3) on the image. Save the image as "squares_with_corners.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path):
    return cv2.imread(image_path)

def find_corners(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)
    return corners

def draw_corners(image, corners):
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
    return image

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def main():
    image_path = Path('./squares.jpg')
    image = load_image(str(image_path))
    corners = find_corners(image)
    image_with_corners = draw_corners(image, corners)
    output_path = Path('./squares_with_corners.png')
    save_image(image_with_corners, str(output_path))

def test():
    assert Path('squares_with_corners.png').exists()

    # load the original image
    original = cv2.imread('squares.jpg')

    corners = find_corners(original)
    image_with_corners = draw_corners(original, corners)

    # load the image with corners
    result = cv2.imread('squares_with_corners.png')

    assert np.array_equal(image_with_corners, result)

    # clean up
    # os.remove('squares_with_corners.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')