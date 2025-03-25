'''
Given an image ("./test_image.png"), compute the gradient magnitude for each pixel using the Sobel operator (ksize=5). Based on the normaliazed gradient values, create a mask where the gradient is above a certain threshold=50. Apply a color overlay to the masked regions (mask weight 0.2, image weight 0.8), enhancing the prominent edges, and save the final image as "edge_overlay.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def compute_gradient_magnitude(image:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    grad = np.sqrt(grad_x**2 + grad_y**2)
    grad = (grad / grad.max() * 255).astype(np.uint8)
    return grad

def create_edge_mask(gradient:np.ndarray, threshold:float) -> np.ndarray:
    return (gradient > threshold).astype(np.uint8) * 255

def color_overlay(image:np.ndarray, mask:np.ndarray, mask_weight:float, image_weight:float) -> np.ndarray:
    return cv2.addWeighted(cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), mask_weight, image, image_weight, 0)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # compute the gradient magnitude
    gradient = compute_gradient_magnitude(image)
    
    # create the edge mask
    mask = create_edge_mask(gradient, 50)
    
    # color overlay
    result = color_overlay(image, mask, 0.2, 0.8).astype(np.uint8)
    
    cv2.imwrite('edge_overlay.png', result)

def test():
    assert Path('edge_overlay.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('edge_overlay.png')
    
    # compute the gradient magnitude
    gradient = compute_gradient_magnitude(image)
    
    # create the edge mask
    mask = create_edge_mask(gradient, 50)
    
    # color overlay
    result_test = color_overlay(image, mask, 0.2, 0.8).astype(np.uint8)
    
    # assert that the images are the same
    assert np.array_equal(result, result_test)

    # clean up
    # os.remove('edge_overlay.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')