'''
Given an image ("./wheres_waldo.jpg") and a template ("./waldo.jpg"), adjust brightness (+50) to the image and perform template matching. Draw a rectangle around the matched region and save the resulting image as "wheres_waldo_matched.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path)
    return image

def adjust_brightness(image:np.ndarray, value:int)->np.ndarray:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def template_matching(image:np.ndarray, template:np.ndarray)->np.ndarray:
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = template.shape[:-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, 255, 2)
    return image

def main()->None:
    image_path = Path('./wheres_waldo.jpg')
    image = load_image(image_path)
    template_path = Path('./waldo.jpg')
    template = load_image(template_path)
    image = adjust_brightness(image, 50)
    result = template_matching(image, template)
    cv2.imwrite('wheres_waldo_matched.png', result)

def test():
    result = cv2.imread('wheres_waldo_matched.png')

    image_path = Path('./wheres_waldo.jpg')
    image = load_image(image_path)
    template_path = Path('./waldo.jpg')
    template = load_image(template_path)
    image = adjust_brightness(image, 50)
    expected = template_matching(image, template)

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('wheres_waldo_matched.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")