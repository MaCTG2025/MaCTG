from Image_Processing import process_image

def test_Image_Processing(image_path: str, output_path: str, threshold_value: int = 200, kernel_size: tuple = (5, 5)) -> None:
    """
    Test the Image_Processing module by processing an image and saving the result.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the final image will be saved.
        threshold_value (int): The brightness threshold value (0-255). Default is 200.
        kernel_size (tuple): The size of the Gaussian kernel. Default is (5, 5).

    Returns:
        None
    """
    # Call the process_image function
    process_image(image_path, output_path, threshold_value, kernel_size)

if __name__ == '__main__':
    # Test the module with a sample image
    test_Image_Processing("./test_image.png", "bright_regions.png")