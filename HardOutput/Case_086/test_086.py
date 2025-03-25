'''
Given an input image ("./test_image.png"), apply artistic effect: pencil sketch effect and highlight object borders, save the output image as "./pencil_sketch_image.png".
'''

import cv2
import numpy as np
import os


def load_image(image_path: str) -> np.ndarray:
    return cv2.imread(image_path)

def pencil_sketch_effect(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = 255 - gray
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    inverted_blurred = 255 - blurred
    sketch = cv2.divide(gray, inverted_blurred, scale=256)
    return sketch

def canny_edge_detection(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges

def combine_images(image: np.ndarray, edges: np.ndarray) -> np.ndarray:
    edge_inv = cv2.bitwise_not(edges)
    edge_rgb = cv2.cvtColor(edge_inv, cv2.COLOR_GRAY2BGR)
    combined = cv2.bitwise_and(image, edge_rgb)
    return combined

def save_image(image: np.ndarray, output_path: str) -> None:
    cv2.imwrite(output_path, image)

def main():
    image = load_image("./test_image.png")
    pencil_sketch = pencil_sketch_effect(image)
    pencil_sketch = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2BGR)
    edges = canny_edge_detection(image)
    combined = combine_images(pencil_sketch, edges)
    save_image(combined, "./pencil_sketch_image.png")

def test():
    assert os.path.exists("./pencil_sketch_image.png")

    result = cv2.imread("./pencil_sketch_image.png")

    image = load_image("./test_image.png")
    pencil_sketch = pencil_sketch_effect(image)
    pencil_sketch = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2BGR)
    edges = canny_edge_detection(image)
    combined = combine_images(pencil_sketch, edges)

    assert np.allclose(combined, result, atol=1)

    # clean up
    # os.remove("./pencil_sketch_image.png")


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")