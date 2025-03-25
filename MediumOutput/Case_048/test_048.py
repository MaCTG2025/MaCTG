'''
Given an image ("./shapes_r.png"), detect shapes using connectedComponentsWithStats (connectivity=8) and then compute the areas and perimeter of the shapes. Save the areas and perimeters into a npy file as "areas_perimeters.npy".
'''


import cv2
from pathlib import Path
import numpy as np
import os

def detect_shapes(image_path:Path) -> tuple:
    image = cv2.imread(str(image_path))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binarized_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binarized_image, connectivity=8)
    areas = stats[1:, cv2.CC_STAT_AREA]
    # manually compute the perimeter
    perimeters = []
    for i in range(1, num_labels):
        mask = np.zeros_like(binarized_image, dtype=np.uint8)
        mask[labels == i] = 255
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        perimeters.append(cv2.arcLength(contours[0], True))
    
    return np.array([areas, perimeters])

def main():
    image_path = Path('./shapes_r.png')
    res = detect_shapes(image_path)
    np.save('areas_perimeters.npy', res)

def test():
    image_path = Path('./shapes_r.png')
    res = detect_shapes(image_path)
    result = np.load('areas_perimeters.npy')

    assert np.array_equal(res, result)

    # clean up
    # os.remove('areas_perimeters.npy')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')