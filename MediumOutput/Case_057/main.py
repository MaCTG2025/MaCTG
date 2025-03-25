from detect_faces_and_apply_edge_enhancement import detect_faces_and_apply_edge_enhancement

def face_detection_and_edge_enhancement(image_path: str, cascade_path: str, output_path: str) -> None:
    """
    Detects faces in the input image, applies edge enhancement to the detected face regions,
    overlays the enhanced edges onto the original image, and saves the result.

    This function serves as the entry point for the module, encapsulating the face detection
    and edge enhancement process.

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar Cascade classifier XML file (e.g., "./haarcascade_frontalface_default.xml").
        output_path (str): Path to save the output image file (e.g., "test_image_faces.png").

    Outputs:
        None: The function saves the processed image to the specified `output_path` and does not return any value.
    """
    detect_faces_and_apply_edge_enhancement(image_path, cascade_path, output_path)

if __name__ == '__main__':
    face_detection_and_edge_enhancement("./test_image.png", "./haarcascade_frontalface_default.xml", "test_image_faces.png")