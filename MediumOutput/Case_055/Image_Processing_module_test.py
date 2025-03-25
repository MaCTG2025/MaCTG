from Image_Processing import image_processing_module

def test_Image_Processing(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the image_processing_module function to ensure it processes the image correctly.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. Example: "./test_image.png".
    output_image_path : str
        The file path where the processed image will be saved. Example: "test_image_filtered.png".

    Returns:
    --------
    None
        The function does not return any value. It simply tests the module functionality.
    """
    # Call the module function
    image_processing_module(input_image_path, output_image_path)
    print(f"Image processing completed. Output saved to {output_image_path}")

if __name__ == '__main__':
    test_Image_Processing("./test_image.png", "test_image_filtered.png")