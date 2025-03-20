'''
Given an image ("./shapes_r.png"), find and extract the largest connected component(not the background), switch all other pixels to black, and save the resulting image as largest_connected_component.png.
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path), 0)

def extract_largest_connected_component(image:np.ndarray) -> np.ndarray:
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)
    largest_component = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
    largest_component_image = np.zeros_like(image)
    largest_component_image[labels == largest_component] = 255
    return largest_component_image

def main():
    image_path = Path('./shapes_r.png')
    image = load_image(image_path)
    
    largest_component_image = extract_largest_connected_component(image)
    
    cv2.imwrite('largest_connected_component.png', largest_component_image)


def test():
    assert Path('largest_connected_component.png').exists()
    
    image = cv2.imread('shapes_r.png', 0)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)
    largest_component = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
    largest_component_image = np.zeros_like(image)
    largest_component_image[labels == largest_component] = 255
    
    assert np.array_equal(cv2.imread('largest_connected_component.png', 0), largest_component_image)
    
    # cleanup
    # os.remove('largest_connected_component.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")