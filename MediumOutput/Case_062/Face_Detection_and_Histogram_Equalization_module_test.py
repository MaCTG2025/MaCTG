from Face_Detection_and_Histogram_Equalization import face_detection_and_histogram_equalization

def test_Face_Detection_and_Histogram_Equalization(image_path: str, cascade_path: str) -> None:
    """
    Tests the functionality of the face_detection_and_histogram_equalization function.

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
        The function does not return any value. It calls the module function 
        and verifies that the output file "test_image_faces.png" is created.
    """
    # Call the module function
    face_detection_and_histogram_equalization(image_path, cascade_path)

    # Verify that the output file is created
    import os
    if os.path.exists("test_image_faces.png"):
        print("Test passed: Output file 'test_image_faces.png' was created successfully.")
    else:
        print("Test failed: Output file 'test_image_faces.png' was not created.")

if __name__ == '__main__':
    test_Face_Detection_and_Histogram_Equalization("./test_image.png", "./haarcascade_frontalface_default.xml")