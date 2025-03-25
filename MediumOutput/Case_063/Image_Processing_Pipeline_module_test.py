import cv2
import numpy as np
from Image_Processing_Pipeline import image_processing_pipeline

def test_Image_Processing_Pipeline():
    """
    Tests the basic functionality of the Image_Processing_Pipeline module.
    """
    # Define input parameters
    image_path = "./test_image.png"  # Path to the test image
    mean = 0.0  # Mean for Gaussian noise
    std_dev = 25.0  # Standard deviation for Gaussian noise
    kernel_size = 5  # Kernel size for median filtering
    output_path = "test_image_corners.png"  # Path to save the output image

    # Call the pipeline function
    image_processing_pipeline(image_path, mean, std_dev, kernel_size, output_path)

    # Verify that the output image is saved
    output_image = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
    assert output_image is not None, "Output image was not saved correctly."

    # Verify that the output image is not empty
    assert output_image.size > 0, "Output image is empty."

    print("Test passed: Image_Processing_Pipeline executed successfully.")

if __name__ == '__main__':
    test_Image_Processing_Pipeline()