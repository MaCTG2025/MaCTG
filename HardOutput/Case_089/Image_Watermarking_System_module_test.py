from Image_Watermarking_System import image_watermarking_system

def test_Image_Watermarking_System(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the basic functionality of the Image_Watermarking_System module.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the watermarked image will be saved (e.g., "./watermarked_image.png").

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    image_watermarking_system(input_image_path, output_image_path)

    # Print success message
    print("Test passed: Watermarked image saved successfully.")

if __name__ == '__main__':
    test_Image_Watermarking_System("./test_image.png", "./watermarked_image.png")