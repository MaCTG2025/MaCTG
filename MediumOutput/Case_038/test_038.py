'''
Given an image ("./wheres_waldo.jpg") and a template image("./waldo_scaled.jpg"), perform multi-scale template matching (template scaling: 0.5x, 0.75x, 1.25x, 1.5x) and find the best match. Draw the bounding box of the best match in red (thickness=3) and save the resulting image as "waldo_scaled_image.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_source_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def load_template_image(template_path:Path) -> np.ndarray:
    return cv2.imread(str(template_path))

def scaling_template(template:np.ndarray, scale:float) -> np.ndarray:
    return cv2.resize(template, (0, 0), fx=scale, fy=scale)

def find_waldo(image:np.ndarray, template:np.ndarray) -> np.ndarray:
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_val, max_loc

def find_best_match(image:np.ndarray, template:np.ndarray) -> np.ndarray:
    scales = [0.5, 0.75, 1.25, 1.5]
    best_match = 0
    best_loc = None
    best_scale = None
    for scale in scales:
        scaled_template = scaling_template(template, scale)
        match, loc = find_waldo(image, scaled_template)
        if match > best_match:
            best_match = match
            best_loc = loc
            best_template = scaled_template
            best_scale = scale
    
    print("Best_scale: ", best_scale)
    h, w = best_template.shape[:2]
    top_left = best_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 3)

    return image

def main():
    image_path = Path('./wheres_waldo.jpg')
    template_path = Path('./waldo_scaled.jpg')

    image = load_source_image(image_path)
    template = load_template_image(template_path)
    best_template = find_best_match(image, template)
    cv2.imwrite('waldo_scaled_image.png', best_template)

def test():
    assert Path('waldo_scaled_image.png').exists()

    # load the waldo scaled image
    result = cv2.imread('waldo_scaled_image.png')
    waldo_scaled_array = find_best_match(load_source_image(Path('./wheres_waldo.jpg')), load_template_image(Path('./waldo_scaled.jpg')))
    
    assert np.array_equal(waldo_scaled_array, result)

    # clean up
    # os.remove('waldo_scaled_image.png')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')
