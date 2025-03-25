'''
Given an image ("./wheres_waldo.jpg"), and the template image ("./waldo.jpg"). Add Gaussian noise to the image (sigma = 1.0, mean = 0.0), then apply template matching (TM_CCOEFF_NORMED) to find the location of the template in the image. Draw a red rectangle (thickness=2) around the detected location and save the result as "wheres_waldo_detected.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def add_gaussian_noise(image:np.ndarray, sigma:float, mean:float) -> np.ndarray:
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    return cv2.add(image, noise)

def template_matching(image:np.ndarray, template:np.ndarray) -> np.ndarray:
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    return max_loc

def draw_rectangle(image:np.ndarray, top_left:tuple, bottom_right:tuple) -> np.ndarray:
    return cv2.rectangle(image.copy(), top_left, bottom_right, (0, 0, 255), 2)

def main():
    image_path = Path('./wheres_waldo.jpg')
    template_path = Path('./waldo.jpg')
    image = load_image(image_path)
    template = load_image(template_path)
    
    # add gaussian noise
    image = add_gaussian_noise(image, 1.0, 0.0)
    
    # template matching
    top_left = template_matching(image, template)
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    
    # draw rectangle
    result = draw_rectangle(image, top_left, bottom_right)
    
    cv2.imwrite('wheres_waldo_detected.png', result)

def test():
    assert Path('wheres_waldo_detected.png').exists()
    
    # load the images
    image = cv2.imread('wheres_waldo.jpg')
    template = cv2.imread('waldo.jpg')
    result = cv2.imread('wheres_waldo_detected.png')
    
    # add gaussian noise
    image = add_gaussian_noise(image, 1.0, 0.0)
    
    # template matching
    top_left = template_matching(image, template)
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    
    # draw rectangle
    result_test = draw_rectangle(image, top_left, bottom_right)
    
    # assert that the images are the same
    assert np.allclose(result, result_test)

    # cleanup
    # os.remove('wheres_waldo_detected.png')

if __name__ == '__main__':
    # main()
    test()
    print("All tests passed")