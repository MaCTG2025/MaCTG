'''
Given an input image ("./test_image.png") and a face cascade file ("./haarcascade_frontalface_default.xml"), detect the face (only one) in the image and draw a rectangle (in red, thickness=2) around it. Save the resulting image as "face_detected.png".
'''

import cv2
from PIL import Image
from pathlib import Path
import os
import numpy as np

def load_image(image_path:Path)->np.ndarray:
    return cv2.imread(image_path)

def detect_face(image:np.ndarray, cascade_path:Path)->np.ndarray:
    face_cascade = cv2.CascadeClassifier(str(cascade_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    return image

def save_image(image:np.ndarray, save_path:Path):
    cv2.imwrite(str(save_path), image)

def main():
    image_path = Path("./test_image.png")
    save_path = Path("./face_detected.png")
    cascade_path = Path("./haarcascade_frontalface_default.xml")

    image = load_image(image_path)
    image = detect_face(image, cascade_path)
    save_image(image, save_path)

def test():
    save_path = Path("./face_detected.png")
    assert save_path.exists(), f"{save_path} does not exist"
    input_image = cv2.imread("./test_image.png")
    cascade_path = Path("./haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(str(cascade_path))
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(input_image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    output_image = cv2.imread("./face_detected.png")
    assert np.array_equal(input_image, output_image), f"Expected {input_image} but got {output_image}"
    # cleanup
    # os.remove(save_path)

if __name__=="__main__":
    # main()
    test()
    print("All tests passed.")