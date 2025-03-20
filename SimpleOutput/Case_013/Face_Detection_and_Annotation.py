from detect_and_annotate_face import detect_and_annotate_face

def face_detection_and_annotation_module(image_path: str, cascade_path: str) -> None:
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
    """
    detect_and_annotate_face(image_path, cascade_path)