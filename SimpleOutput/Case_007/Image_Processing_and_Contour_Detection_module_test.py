from Image_Processing_and_Contour_Detection import process_image_and_detect_contours
import numpy as np

def test_Image_Processing_and_Contour_Detection(image_path: str, output_path: str, threshold: int = 128) -> None:
    """
    Tests the functionality of the Image_Processing_and_Contour_Detection module.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the resulting image with contours.
        threshold (int, default=128): Threshold value for binarization.
    """
    # Test the module function
    contours_image = process_image_and_detect_contours(image_path, output_path, threshold)
    
    # Check output type
    assert isinstance(contours_image, np.array), "Output is not a NumPy array."
    
    # Check if the output image is saved correctly
    import os
    assert os.path.exists(output_path), "Output image file was not created."
    
    print("Test passed: Output is a NumPy array and the image file was saved successfully.")

if __name__ == '__main__':
    test_Image_Processing_and_Contour_Detection("./test_image.png", "contours_image.png")