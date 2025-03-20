from Face_Detection_and_Annotation import face_detection_and_annotation_module

def test_Face_Detection_and_Annotation(image_path: str, cascade_path: str) -> None:
    """
    Tests the face_detection_and_annotation_module function to ensure it detects a face,
    annotates it with a red rectangle, and saves the resulting image as 'face_detected.png'.

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
        The function does not return any value. It prints a success message if the test passes.
    """
    face_detection_and_annotation_module(image_path, cascade_path)
    print("Test passed: 'face_detected.png' was successfully created.")

if __name__ == '__main__':
    test_Face_Detection_and_Annotation("./test_image.png", "./haarcascade_frontalface_default.xml")