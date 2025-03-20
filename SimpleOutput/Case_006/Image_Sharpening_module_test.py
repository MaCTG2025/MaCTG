from Image_Sharpening import sharpen_image

def test_Image_Sharpening(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Image_Sharpening module.

    Args:
        input_image_path (str): The file path of the input image to be processed.
        output_image_path (str): The file path where the sharpened image will be saved.

    Returns:
        None
    """
    try:
        sharpen_image(input_image_path, output_image_path)
        print("Test passed: Image sharpening completed successfully.")
    except FileNotFoundError:
        print("Test failed: Input image file not found.")
    except ValueError as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Sharpening("./test_image.png", "sharpened_image.png")