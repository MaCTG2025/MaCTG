from Image_Processing import image_processing_module

def test_Image_Processing(input_image_path: str, output_image_path: str, blockSize: int = 11, C: int = 2) -> None:
    """
    Tests the functionality of the `image_processing_module` function.

    This test function verifies that the module processes an input image correctly by:
    1. Converting the image to grayscale.
    2. Applying adaptive thresholding.
    3. Saving the resulting binary image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the processed binary image will be saved.
    blockSize : int, optional (default=11)
        The size of a pixel neighborhood used to calculate a threshold value for the pixel.
    C : int, optional (default=2)
        A constant subtracted from the mean or weighted mean to fine-tune the thresholding.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    image_processing_module(input_image_path, output_image_path, blockSize, C)
    print(f"Test passed: Binary image saved to {output_image_path}")

if __name__ == '__main__':
    # Test the module with default parameters
    test_Image_Processing("./test_image.png", "binary_image.png")