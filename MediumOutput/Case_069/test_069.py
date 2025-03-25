'''
Given an image ("./test_image.png"), rescale it to 2x size using linear and cubic interpolation, detect contours in red(thickness=3) on both rescaled images, and save the results as "rescaled_linear.png" and "rescaled_cubic.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def rescale_image(image:np.ndarray, scale:float, interpolation=cv2.INTER_LINEAR) -> np.ndarray:
    return cv2.resize(image, (0, 0), fx=scale, fy=scale, interpolation=interpolation)

def detect_contours(image:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image:np.ndarray, contours:np.ndarray) -> np.ndarray:
    return cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # rescale the image
    rescaled_linear = rescale_image(image, 2, cv2.INTER_LINEAR)
    rescaled_cubic = rescale_image(image, 2, cv2.INTER_CUBIC)
    
    # detect contours
    contours_linear = detect_contours(rescaled_linear)
    contours_cubic = detect_contours(rescaled_cubic)
    
    # draw the contours
    rescaled_linear = draw_contours(rescaled_linear, contours_linear)
    rescaled_cubic = draw_contours(rescaled_cubic, contours_cubic)
    
    cv2.imwrite('rescaled_linear.png', rescaled_linear)
    cv2.imwrite('rescaled_cubic.png', rescaled_cubic)

def test():
    assert Path('rescaled_linear.png').exists()
    assert Path('rescaled_cubic.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    rescaled_linear = cv2.imread('rescaled_linear.png')
    rescaled_cubic = cv2.imread('rescaled_cubic.png')
    
    # rescale the image
    rescaled_linear_test = rescale_image(image, 2, cv2.INTER_LINEAR)
    rescaled_cubic_test = rescale_image(image, 2, cv2.INTER_CUBIC)
    
    # detect contours
    contours_linear = detect_contours(rescaled_linear_test)
    contours_cubic = detect_contours(rescaled_cubic_test)
    
    # draw the contours
    rescaled_linear_test = draw_contours(rescaled_linear_test, contours_linear)
    rescaled_cubic_test = draw_contours(rescaled_cubic_test, contours_cubic)
    
    # assert that the images are the same
    assert np.array_equal(rescaled_linear, rescaled_linear_test)
    assert np.array_equal(rescaled_cubic, rescaled_cubic_test)
    
    # clean up
    # os.remove('rescaled_linear.png')
    # os.remove('rescaled_cubic.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')