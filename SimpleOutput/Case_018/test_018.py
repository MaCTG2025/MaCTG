'''
Given an input image ("./someshapes.jpg"), there is a rectangle, a square, a triangle, a circle and a star in the image. Find these shapes and draw the contours of the shape in different colors (thickness=2): red for the rectangle, green for the square, blue for the triangle, yellow for the circle and pink for the star. Save the resulting image as "shapes_image.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(str(image_path))

def find_shapes(image:np.ndarray)->np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours[1:]:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            # square
            if abs(abs(approx[0][0][0] - approx[1][0][0]) - abs(approx[2][0][1] - approx[1][0][1])) < 5:
                cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
            # rectangle
            else:
                cv2.drawContours(image, [contour], 0, (0, 0, 255), 2)
        elif len(approx) == 3:
            cv2.drawContours(image, [contour], 0, (255, 0, 0), 2)
        elif len(approx) == 10:
            cv2.drawContours(image, [contour], 0, (255, 0, 255), 2)
        elif len(approx) > 10:
            cv2.drawContours(image, [contour], 0, (0, 255, 255), 2)
    return image

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./someshapes.jpg")
    save_path = Path("./shapes_image.png")

    image = load_image(image_path)
    image = find_shapes(image)
    save_image(image, save_path)

def test():
    save_path = Path("./shapes_image.png")
    assert save_path.exists(), f"{save_path} does not exist"
    input_image = cv2.imread("./someshapes.jpg")
    output_image = find_shapes(input_image)
    result = cv2.imread("./shapes_image.png")
    assert np.array_equal(result, output_image), f"Expected {result} but got {output_image}"
    # cleanup
    # os.remove(save_path)

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')