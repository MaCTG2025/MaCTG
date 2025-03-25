'''
Given an image ("./test_image.png"), perform pyramid downscaling (factor x1, x0.5, x0.25) and apply Shi-Tomasi corner detection at each scale (maxCorners=100, qualityLevel=0.01, minDistance=10 and blockSize=3). Save the resulting images as "test_image_corners_x1.png", "test_image_corners_x0.5.png" and "test_image_corners_x0.25.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path:Path):
    return cv2.imread(str(image_path))

def detect_corners(image:np.ndarray, scale:float):
    resized = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10, blockSize=3)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(resized, (x, y), 3, (0, 0, 255), -1)

    return resized

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)

    scales = [1, 0.5, 0.25]
    for scale in scales:
        corners = detect_corners(image, scale)
        cv2.imwrite(f'./test_image_corners_x{scale}.png', corners)

def test():
    for scale in [1, 0.5, 0.25]:
        assert Path(f'./test_image_corners_x{scale}.png').exists()

        result = cv2.imread(f'./test_image_corners_x{scale}.png')
        assert result is not None

        image = load_image(Path('./test_image.png'))
        assert image is not None

        corners_img = detect_corners(image, scale)

        assert np.array_equal(result, corners_img)

        # cleanup
        # os.remove(f'./test_image_corners_x{scale}.png')
    
if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')