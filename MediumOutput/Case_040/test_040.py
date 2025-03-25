'''
Given an input image ("./test_image.png"), use bilateral filtering with d = 9, sigmaColor = 75, sigmaSpace = 75, and apply multi-level Canny edge detection with thresholds at low = 50, medium = 100, and high = 150, blending the edges together and the stylized image with a weight of 0.8 for the stylized image and 0.2 for the edges. Save the resulting image as "bilateral_canny_image.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os
from typing import List

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def apply_bilateral_filter(image:np.ndarray, d:int, sigmaColor:float, sigmaSpace:float) -> np.ndarray:
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

def multi_level_canny_edge_detection(image:np.ndarray, low:int, medium:int, high:int) -> np.ndarray:
    edges_low = cv2.Canny(image, low, medium)
    edges_medium = cv2.Canny(image, medium, high)
    edges_high = cv2.Canny(image, high, high)
    return cv2.cvtColor(edges_low, cv2.COLOR_GRAY2BGR), cv2.cvtColor(edges_medium, cv2.COLOR_GRAY2BGR), cv2.cvtColor(edges_high, cv2.COLOR_GRAY2BGR)

def blend_images(image:np.ndarray, edges:List[np.ndarray], weight_image:float, weight_edges:float) -> np.ndarray:
    for edge in edges:
        image = cv2.addWeighted(image, weight_image, edge, weight_edges, 0)

    return image

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    stylized_image = apply_bilateral_filter(image, 9, 75, 75)
    edges_low, edges_medium, edges_high = multi_level_canny_edge_detection(stylized_image, 50, 100, 150)
    blended_image = blend_images(stylized_image, [edges_low, edges_medium, edges_high], 0.8, 0.2)
    cv2.imwrite('bilateral_canny_image.png', blended_image)

def test():
    assert Path('bilateral_canny_image.png').exists()

    image = load_image(Path('./test_image.png'))
    stylized_image = apply_bilateral_filter(image, 9, 75, 75)
    edges_low, edges_medium, edges_high = multi_level_canny_edge_detection(stylized_image, 50, 100, 150)
    blended_image = blend_images(stylized_image, [edges_low, edges_medium, edges_high], 0.8, 0.2)
    result = cv2.imread('bilateral_canny_image.png')

    assert np.array_equal(blended_image, result)

    # clean up
    # os.remove('bilateral_canny_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')
