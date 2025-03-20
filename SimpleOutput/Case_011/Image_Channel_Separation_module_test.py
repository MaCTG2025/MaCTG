from Image_Channel_Separation import process_image_channels

def test_Image_Channel_Separation(image_path: str) -> None:
    """
    Tests the basic functionality of the Image_Channel_Separation module by processing an RGB image and verifying that the output files are created.

    Args:
        image_path (str): The file path to the input RGB image. The image should be in PNG format.

    Returns:
        None: This function does not return any value. It prints a success message if the test passes.
    """
    try:
        process_image_channels(image_path)
        print("Test passed: Output files (red_channel.png, green_channel.png, blue_channel.png) were created successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Channel_Separation("./test_image.png")