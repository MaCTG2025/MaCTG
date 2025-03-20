'''
Given an input image ("./wheres_waldo.jpg") and a template image ("./waldo.jpg"), find the the template image in the input image. Draw the bounding box of the match in red and save the resulting image as "waldo_image.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def find_match(image:np.ndarray, template:np.ndarray)->np.ndarray:
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    h, w = template.shape[:2]
    return cv2.rectangle(image.copy(), max_loc, (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)

def save_image(image:np.ndarray, output_path:Path):
    cv2.imwrite(str(output_path), image)


def main():
    image_path = Path('./wheres_waldo.jpg')
    template_path = Path('./waldo.jpg')
    image = load_image(image_path)
    template = load_image(template_path)
    matched_image = find_match(image, template)
    save_image(matched_image, Path('./waldo_image.png'))

def test():
    assert Path('waldo_image.png').exists()

    # load the original image
    original = cv2.imread('wheres_waldo.jpg')
    template = cv2.imread('waldo.jpg')

    matched = find_match(original, template)

    # load the image with corners
    matched_result = cv2.imread('waldo_image.png')

    assert np.array_equal(matched, matched_result)

    # clean up
    # os.remove('waldo_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')