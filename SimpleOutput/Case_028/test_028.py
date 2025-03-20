'''
Given an input image ("./test_image.png"), draw an green ellipse with fixed parameters (center=(100, 100), axes=(100, 50), angle=45, thickness=2) on the image and save the resulting image as ellipse.png.
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def draw_ellipse(image:np.ndarray) -> np.ndarray:
    return cv2.ellipse(image, (100, 100), (100, 50), 45, 0, 360, (0, 255, 0), 2)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    ellipse_image = draw_ellipse(image)
    
    cv2.imwrite('ellipse.png', ellipse_image)


def test():
    assert Path('ellipse.png').exists()
    
    image = cv2.imread('test_image.png')
    ellipse_image = cv2.ellipse(image, (100, 100), (100, 50), 45, 0, 360, (0, 255, 0), 2)
    
    assert np.array_equal(cv2.imread('ellipse.png'), ellipse_image)
    
    # cleanup
    # os.remove('ellipse.png')


if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")