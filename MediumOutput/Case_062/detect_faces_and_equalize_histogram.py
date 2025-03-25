import cv2
import numpy as np

def detect_faces_and_equalize_histogram(image_path: str, cascade_path: str) -> None:
    """
    Detects faces in the input image using the provided Haar Cascade classifier, 
    applies histogram equalization to the detected face regions, and saves the 
    processed image as "test_image_faces.png".

    Parameters:
    -----------
    image_path : str
        The file path to the input image where faces need to be detected.
        Example: "./test_image.png"

    cascade_path : str
        The file path to the Haar Cascade classifier XML file.
        Example: "./haarcascade_frontalface_default.xml"

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image 
        with histogram equalization applied to the detected face regions as 
        "test_image_faces.png" in the current working directory.

    Requirements:
    -------------
    1. The input image must be a valid image file (e.g., PNG, JPG).
    2. The Haar Cascade classifier file must be a valid XML file.
    3. The function uses OpenCV for face detection and histogram equalization.
    4. If no faces are detected, the function will save the original image 
       without any modifications.

    Example:
    --------
    detect_faces_and_equalize_histogram("./test_image.png", "./haarcascade_frontalface_default.xml")
    """
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each face
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Apply histogram equalization
        equ = cv2.equalizeHist(roi_gray)

        # Replace the original ROI with the equalized one
        img[y:y+h, x:x+w] = cv2.cvtColor(cv2.merge((equ, equ, equ)), cv2.COLOR_BGR2RGB)

    # Save the result
    cv2.imwrite("test_image_faces.png", img)