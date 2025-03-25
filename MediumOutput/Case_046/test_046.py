'''
Given an image ("./test_image.png"), crop central 75% of the image and apply a perspective transformation to the cropped region (input points are the 4 corners of the cropped region, output points are [[10, 100], [10, 250], [300, 300], [300, 200]]). Save the resulting image as "perspective_transformed_image.png".
'''


import cv2
from pathlib import Path
import numpy as np
import os


def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def crop_center(image:np.ndarray, crop_percent:int) -> np.ndarray:
    h, w = image.shape[:2]
    crop_size = int(min(h, w) * crop_percent / 100)
    center = (w//2, h//2)
    return image[center[1]-crop_size//2:center[1]+crop_size//2, center[0]-crop_size//2:center[0]+crop_size//2]

def apply_perspective_transform(image:np.ndarray) -> np.ndarray:
    h, w = image.shape[:2]
    input_points = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)
    output_points = np.array([[10, 100], [10, 250], [300, 300], [300, 200]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(input_points, output_points)
    return cv2.warpPerspective(image, M, (w, h))

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    cropped_image = crop_center(image, 75)
    perspective_transformed_image = apply_perspective_transform(cropped_image)
    cv2.imwrite('perspective_transformed_image.png', perspective_transformed_image)

def test():
    assert Path('perspective_transformed_image.png').exists()

    image = load_image(Path('./test_image.png'))
    cropped_image = crop_center(image, 75)
    perspective_transformed_image = apply_perspective_transform(cropped_image)
    result = cv2.imread('perspective_transformed_image.png')
    assert np.array_equal(perspective_transformed_image, result)

    # clean up
    # os.remove('perspective_transformed_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')