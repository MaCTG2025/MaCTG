'''
Given an image ("./test_image.png"), detect faces using "./haarcascade_frontalface_default.xml" and apply histogram equalization on the face region, save the resulting image as "test_image_faces.png".
'''

import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(str(image_path))
    return image

def face_detection(image:np.ndarray)->np.ndarray:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def apply_histogram_equalization(image:np.ndarray)->np.ndarray:
    return cv2.equalizeHist(image)

def apply_histogram_equalization_on_faces(image:np.ndarray, faces:np.ndarray)->np.ndarray:
    for (x, y, w, h) in faces:
        # do histogram equalization on the each channel
        for i in range(3):
            image[y:y+h, x:x+w, i] = apply_histogram_equalization(image[y:y+h, x:x+w, i])
    return image

def main()->None:
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    faces = face_detection(image)
    result = apply_histogram_equalization_on_faces(image, faces)
    cv2.imwrite('test_image_faces.png', result)

def test():
    result = cv2.imread('test_image_faces.png')

    image_path = Path('./test_image.png')
    image = load_image(image_path)
    faces = face_detection(image)
    expected = apply_histogram_equalization_on_faces(image, faces)

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('test_image_faces.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")