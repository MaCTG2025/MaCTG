from Image_Corner_Detection_and_Transformation import process_image
import cv2
import numpy as np

def test_Image_Corner_Detection_and_Transformation(image_path: str) -> None:
    """
    Tests the Image_Corner_Detection_and_Transformation module by processing an image and verifying the outputs.

    Args:
        image_path (str): The file path of the input image to be processed.

    Returns:
        None: Prints a success message if the test passes.
    """
    # Process the image
    process_image(image_path)

    # Verify that the output files were created
    original_image = cv2.imread("original_image.png")
    rotated_back_image = cv2.imread("rotated_image_back.png")

    # Check if the images were saved correctly
    assert original_image is not None, "Failed to save the original image with corners."
    assert rotated_back_image is not None, "Failed to save the rotated back image."

    # Print success message
    print("Test passed: The images were processed and saved correctly.")

if __name__ == '__main__':
    test_Image_Corner_Detection_and_Transformation("./test_image.png")