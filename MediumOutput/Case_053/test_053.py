'''
Given an image ("./wheres_waldo.jpg") and a rotated template image ("./waldo_rotate.jpg"), apply a rotation-invariant template matching algorithm by trying [0, 45, 90, 135] degrees to find the template in the image. Draw a rectangle around the template (thickness=2) in the image and save the resulting image as "wheres_waldo_found.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path, template_path:Path):
    return cv2.imread(str(image_path)), cv2.imread(str(template_path))

def find_template(image:np.ndarray, template:np.ndarray):
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_loc, max_val

def rotate_template(template:np.ndarray, angle:int):
    h, w, _ = template.shape
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(template, M, (w, h))

    return rotated

def main():
    image_path = Path('./wheres_waldo.jpg')
    template_path = Path('./waldo_rotate.jpg')
    image, template = load_image(image_path, template_path)

    best_loc = None
    best_angle = None
    best_val = -1

    for angle in [0, 45, 90, 135]:
        rotated_template = rotate_template(template, angle)
        loc, val = find_template(image, rotated_template)
        if val > best_val:
            best_loc = loc
            best_angle = angle
            best_val = val

    print(f'Best angle: {best_angle}')
    h, w, _ = rotated_template.shape
    cv2.rectangle(image, best_loc, (best_loc[0]+w, best_loc[1]+h), (0, 0, 255), 2)
    cv2.imwrite('./wheres_waldo_found.png', image)

def test():
    assert Path('./wheres_waldo_found.png').exists()

    result = cv2.imread('./wheres_waldo_found.png')
    image, template = load_image(Path('./wheres_waldo.jpg'), Path('./waldo_rotate.jpg'))

    best_loc = None
    best_angle = None
    best_val = -1

    for angle in [0, 45, 90, 135]:
        rotated_template = rotate_template(template, angle)
        loc, val = find_template(image, rotated_template)
        if val > best_val:
            best_loc = loc
            best_angle = angle
            best_val = val

    h, w, _ = rotated_template.shape
    cv2.rectangle(image, best_loc, (best_loc[0]+w, best_loc[1]+h), (0, 0, 255), 2)

    assert np.array_equal(image, result)

    # clean up
    # os.remove('./wheres_waldo_found.png')

if __name__ == '__main__':
    main()
    test()
    print('All tests passed')