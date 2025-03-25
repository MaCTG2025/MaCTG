import numpy as np
from Image_Processing_Module import image_processing_module

def test_image_processing_module() -> None:
    """
    Tests the functionality of the image_processing_module function.
    """
    # Define input parameters
    image_path = "./test_image.png"
    sharpening_kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    gaussian_kernel_size = (5, 5)
    sigmaX = 5
    output_path = "sharpened_gaussian_image.png"

    # Call the module function
    image_processing_module(
        image_path=image_path,
        sharpening_kernel=sharpening_kernel,
        gaussian_kernel_size=gaussian_kernel_size,
        sigmaX=sigmaX,
        output_path=output_path
    )

    # Print success message
    print("Test completed successfully. Check the output image at:", output_path)

if __name__ == '__main__':
    test_image_processing_module()