from detect_faces_and_equalize_histogram import detect_faces_and_equalize_histogram

def face_detection_and_histogram_equalization(image_path: str, cascade_path: str) -> None:
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
    """
    detect_faces_and_equalize_histogram(image_path, cascade_path)