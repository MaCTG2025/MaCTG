'''
Given an image ("./test_image.png"), perform Canny edge detection (threshold1 = 100, threshold2 = 200), identify the enclosed regions using contour detection, and fill these regions with a solid color (e.g., green) while keeping the edges visible, then save the final image as "filled_regions.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def canny_edge_detection(image:np.ndarray, threshold1:int, threshold2:int) -> np.ndarray:
    return cv2.Canny(image, threshold1, threshold2)

def find_contours(image:np.ndarray) -> np.ndarray:
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def fill_regions(image:np.ndarray, contours:np.ndarray, color:tuple) -> np.ndarray:
    return cv2.drawContours(image, contours, -1, color, thickness=cv2.FILLED)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # perform Canny edge detection
    edges = canny_edge_detection(image, 100, 200)
    
    # identify the enclosed regions using contour detection
    contours = find_contours(edges)
    
    # fill the regions with a solid color
    result = fill_regions(image.copy(), contours, (0, 255, 0))
    
    cv2.imwrite('filled_regions.png', result)

def test():
    assert Path('filled_regions.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('filled_regions.png')
    
    # perform Canny edge detection
    edges = canny_edge_detection(image, 100, 200)
    
    # identify the enclosed regions using contour detection
    contours = find_contours(edges)
    
    # fill the regions with a solid color
    result_test = fill_regions(image.copy(), contours, (0, 255, 0))
    
    # assert that the images are the same
    assert np.allclose(result, result_test)

    # clean up
    # os.remove('filled_regions.png')

if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")