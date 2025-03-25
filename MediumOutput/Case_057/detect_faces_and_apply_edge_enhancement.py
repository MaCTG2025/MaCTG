import cv2
import numpy as np

def detect_faces_and_apply_edge_enhancement(image_path: str, cascade_path: str, output_path: str) -> None:
    """
    Detects faces in the input image using the Haar Cascade classifier, applies edge enhancement
    to the detected face regions, overlays the enhanced edges onto the original image, and saves the result.

    Steps:
    1. Load the input image from the specified `image_path`.
    2. Load the Haar Cascade classifier from the specified `cascade_path`.
    3. Detect faces in the image using the Haar Cascade classifier.
    4. For each detected face:
        a. Extract the face region from the image.
        b. Apply edge enhancement (sharpening) using the kernel [[0, -1, 0], [-1, 5, -1], [0, -1, 0]].
        c. Overlay the enhanced edges onto the original image.
    5. Save the resulting image to the specified `output_path`.

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar Cascade classifier XML file (e.g., "./haarcascade_frontalface_default.xml").
        output_path (str): Path to save the output image file (e.g., "test_image_faces.png").

    Outputs:
        None: The function saves the processed image to the specified `output_path` and does not return any value.

    Requirements:
        - The input image must be a valid image file (e.g., PNG, JPG).
        - The Haar Cascade classifier file must be valid and compatible with OpenCV.
        - The output directory must exist, or the function will raise an error.

    Dependencies:
        - OpenCV (cv2) for image processing and face detection.
        - NumPy (numpy) for matrix operations during edge enhancement.

    Example Usage:
        detect_faces_and_apply_edge_enhancement("./test_image.png", "./haarcascade_frontalface_default.xml", "test_image_faces.png")
    """
    # Load the input image
    image = cv2.imread(image_path)
    
    # Load the Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Define the sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    # Process each detected face
    for (x, y, w, h) in faces:
        # Extract the face region
        face_region = image[y:y+h, x:x+w]
        
        # Apply edge enhancement
        sharpened_face = cv2.filter2D(face_region, -1, kernel)
        
        # Overlay the enhanced edges onto the original image
        image[y:y+h, x:x+w] = sharpened_face
    
    # Save the resulting image
    cv2.imwrite(output_path, image)