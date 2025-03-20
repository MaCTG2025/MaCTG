import cv2

def detect_and_annotate_face(image_path: str, cascade_path: str) -> None:
    """
    Detects a single face in the input image using the provided face cascade file, 
    draws a red rectangle (thickness=2) around the detected face, and saves the 
    resulting image as 'face_detected.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image where the face detection will be performed.
        Example: "./test_image.png"

    cascade_path : str
        The file path to the Haar Cascade XML file used for face detection.
        Example: "./haarcascade_frontalface_default.xml"

    Returns:
    --------
    None
        The function does not return any value. It saves the resulting image with 
        the detected face annotated as 'face_detected.png' in the current working directory.

    Requirements:
    -------------
    1. The input image must exist at the specified `image_path`.
    2. The Haar Cascade file must exist at the specified `cascade_path`.
    3. Only one face is expected in the input image. If multiple faces are detected, 
       only the first one will be annotated.
    4. The rectangle drawn around the face will be red (BGR color: (0, 0, 255)) with 
       a thickness of 2 pixels.
    5. The resulting image will be saved as 'face_detected.png' in the current directory.

    Dependencies:
    -------------
    - OpenCV (cv2) must be installed and imported.

    Example Usage:
    --------------
    detect_and_annotate_face("./test_image.png", "./haarcascade_frontalface_default.xml")
    """
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the input image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around the first detected face
    if len(faces) > 0:
        x, y, w, h = faces[0]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Save the output image
    cv2.imwrite('face_detected.png', img)