from Face_Detection_and_Edge_Enhancement import face_detection_and_edge_enhancement

def test_Face_Detection_and_Edge_Enhancement(image_path: str, cascade_path: str, output_path: str) -> None:
    """
    Tests the basic functionality of the Face Detection and Edge Enhancement module.

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar Cascade classifier XML file (e.g., "./haarcascade_frontalface_default.xml").
        output_path (str): Path to save the output image file (e.g., "test_image_faces.png").

    Outputs:
        None: The function tests the module and does not return any value.
    """
    # Call the module function
    face_detection_and_edge_enhancement(image_path, cascade_path, output_path)
    print(f"Test completed. Output saved to {output_path}.")

if __name__ == '__main__':
    test_Face_Detection_and_Edge_Enhancement("./test_image.png", "./haarcascade_frontalface_default.xml", "test_image_faces.png")