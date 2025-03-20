from Blob_Detection_and_Bounding_Box_Drawing import blob_detection_module

def test_Blob_Detection_and_Bounding_Box_Drawing(image_path: str) -> None:
    """
    Test the functionality of the blob_detection_module by detecting blobs in the input image,
    drawing bounding boxes around them, and saving the resulting image.

    Parameters:
    -----------
    image_path : str
        The file path to the input image where blobs need to be detected.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the function runs without errors.
    """
    try:
        blob_detection_module(image_path)
        print("Test passed: The function executed successfully and saved the output image as 'blobs_image.png'.")
    except Exception as e:
        print(f"Test failed: An error occurred during execution - {e}")

if __name__ == '__main__':
    test_Blob_Detection_and_Bounding_Box_Drawing("./blobs.jpg")