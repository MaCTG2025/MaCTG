'''
Given an image ("./test_image.png"), detect faces using ("./haarcascade_frontalface_default.xml") and apply edge enhancement (sharpening with kernel [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) on the face region and add the edge on the original image. Save the resulting image as "test_image_faces.png".
'''


import cv2
import numpy as np
from pathlib import Path
import os


def load_image(image_path:Path)->np.ndarray:
    image = cv2.imread(image_path)
    return image

def face_detection(image:np.ndarray)->np.ndarray:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def sharpen_image(image:np.ndarray)->np.ndarray:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def blend_images(image:np.ndarray, sharpened:np.ndarray, faces:np.ndarray)->np.ndarray:
    for (x, y, w, h) in faces:
        image[y:y+h, x:x+w] = sharpened[y:y+h, x:x+w]
    return image

def main()->None:
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    faces = face_detection(image)
    sharpened = sharpen_image(image)
    result = blend_images(image, sharpened, faces)
    cv2.imwrite('test_image_faces.png', result)

def test():
    result = cv2.imread('test_image_faces.png')

    image_path = Path('./test_image.png')
    image = load_image(image_path)
    faces = face_detection(image)
    sharpened = sharpen_image(image)
    expected = blend_images(image, sharpened, faces)

    assert np.array_equal(result, expected)

    # cleanup
    # os.remove('test_image_faces.png')


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")
