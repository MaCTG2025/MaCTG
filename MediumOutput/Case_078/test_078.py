'''
Given an image ("./test_image.png"), rotate the image by 90 degrees, compute the gradient magnitude for both the original and rotated images using the Sobel operator(ksize=5). Compare the gradient magnitude and save the difference using a heatmap to highlight areas of similarity and difference as "difference_heatmap.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def rotate_image(image:np.ndarray, angle:float) -> np.ndarray:
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def compute_gradient_magnitude(image:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    grad = np.sqrt(grad_x**2 + grad_y**2)
    grad = (grad / grad.max() * 255).astype(np.uint8)
    return grad


def compute_difference_image(image1:np.ndarray, image2:np.ndarray) -> np.ndarray:
    return cv2.absdiff(image1, image2)

def draw_heatmap(image:np.ndarray) -> np.ndarray:
    heatmap = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    return heatmap

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    
    # rotate the image
    rotated = rotate_image(image, 90)
    
    # compute the gradient magnitude
    gradient = compute_gradient_magnitude(image)
    gradient_rotated = compute_gradient_magnitude(rotated)

    # compute the difference image
    difference = compute_difference_image(gradient, gradient_rotated)

    # draw the heatmap
    heatmap = draw_heatmap(difference)
    cv2.imwrite('difference_heatmap.png', heatmap)

def test():
    assert Path('difference_heatmap.png').exists()
    
    # load the images
    image = cv2.imread('test_image.png')
    result = cv2.imread('difference_heatmap.png')
    
    # rotate the image
    rotated = rotate_image(image, 90)
    
    # compute the gradient magnitude
    gradient = compute_gradient_magnitude(image)
    gradient_rotated = compute_gradient_magnitude(rotated)

    # compute the difference image
    difference = compute_difference_image(gradient, gradient_rotated)

    # draw the heatmap
    heatmap = draw_heatmap(difference)
    assert np.array_equal(result, heatmap)
    # assert that the images are the same
    assert np.array_equal(result, heatmap)

    # clean up
    # os.remove('difference_heatmap.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')