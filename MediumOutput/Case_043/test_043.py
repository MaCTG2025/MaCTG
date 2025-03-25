'''
Given an image ("./test_image.png"), detect faces using Haar cascades (scaleFactor = 1.1, minNeighbors = 5) using "./haarcascade_frontalface_default.xml" and apply Gaussian blur (25x25) to the background, Save the resulting image as "final_image.png".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def detect_faces(image:np.ndarray, cascade_path:Path) -> np.ndarray:
    face_cascade = cv2.CascadeClassifier(str(cascade_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces

def apply_gaussian_blur(image:np.ndarray, kernel_size:int, sigmaX:float) -> np.ndarray:
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)

def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    faces = detect_faces(image, Path('./haarcascade_frontalface_default.xml'))
    mask = np.zeros_like(image)
    for (x, y, w, h) in faces:
        mask[y:y+h, x:x+w] = 255
    blurred_image = apply_gaussian_blur(image, 25, 25)
    blurred_image[np.where(mask == 255)] = image[np.where(mask == 255)]
    cv2.imwrite('final_image.png', blurred_image)

def test():
    assert Path('final_image.png').exists()

    image = load_image(Path('./test_image.png'))
    faces = detect_faces(image, Path('./haarcascade_frontalface_default.xml'))
    mask = np.zeros_like(image)
    for (x, y, w, h) in faces:
        mask[y:y+h, x:x+w] = 255
    blurred_image = apply_gaussian_blur(image, 25, 25)
    blurred_image[np.where(mask == 255)] = image[np.where(mask == 255)]
    result = cv2.imread('final_image.png')
    assert np.array_equal(blurred_image, result)

    # clean up
    # os.remove('final_image.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')