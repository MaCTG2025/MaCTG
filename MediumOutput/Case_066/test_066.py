'''
Given an image ("./texture_seg.png"), divide the image into four fixed regions (top-left, top-right, bottom-left, and bottom-right). Apply flood fill starting from the center of each region to grow the region based on gradient similarity (threshold = 30). Highlighting the different regions with the following colors: red, green, blue, and yellow. Save the result as "segmented_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def divide_image(image:np.ndarray) -> list:
    h, w = image.shape[:2]
    top_left = image[:h//2, :w//2]
    top_right = image[:h//2, w//2:]
    bottom_left = image[h//2:, :w//2]
    bottom_right = image[h//2:, w//2:]
    return [top_left, top_right, bottom_left, bottom_right]

def apply_flood_fill(image:np.ndarray, seed:tuple, color:tuple, threshold:int) -> np.ndarray:
    mask = np.zeros((image.shape[0]+2, image.shape[1]+2), np.uint8)
    cv2.floodFill(image, mask, seed, color, (threshold,)*3, (threshold,)*3, cv2.FLOODFILL_FIXED_RANGE)
    return image

def main():
    image_path = Path('./texture_seg.png')
    image = load_image(image_path)
    
    # divide the image into four fixed regions
    regions = divide_image(image)
    
    # apply flood fill starting from the center of each region
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]
    seeds = [(regions[i].shape[1]//2, regions[i].shape[0]//2) for i in range(4)]
    threshold = 30
    for i in range(4):
        regions[i] = apply_flood_fill(regions[i], seeds[i], colors[i], threshold)
    
    # merge the regions
    segmented_image = np.vstack([np.hstack([regions[0], regions[1]]), np.hstack([regions[2], regions[3]])])
    
    # save the segmented image
    cv2.imwrite('segmented_image.png', segmented_image)


def test():
    assert Path('segmented_image.png').exists()
    
    # load the image
    image = cv2.imread('texture_seg.png')
    
    # divide the image into four fixed regions
    regions = divide_image(image)
    
    # apply flood fill starting from the center of each region
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]
    seeds = [(regions[i].shape[1]//2, regions[i].shape[0]//2) for i in range(4)]
    threshold = 30
    for i in range(4):
        regions[i] = apply_flood_fill(regions[i], seeds[i], colors[i], threshold)
    
    # merge the regions
    segmented_image = np.vstack([np.hstack([regions[0], regions[1]]), np.hstack([regions[2], regions[3]])])
    
    # load the segmented image
    segmented_image_test = cv2.imread('segmented_image.png')
    
    # assert that the images are the same
    assert np.array_equal(segmented_image, segmented_image_test)

    # clean up
    # os.remove('segmented_image.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")