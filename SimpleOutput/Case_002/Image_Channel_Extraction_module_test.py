from Image_Channel_Extraction import process_image_channels

def test_Image_Channel_Extraction(image_path: str) -> None:
    """
    Tests the functionality of the Image_Channel_Extraction module by processing an RGB image and verifying that the output images are saved correctly.

    Parameters:
    -----------
    image_path : str
        The file path to the input RGB image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the function to process the image
    process_image_channels(image_path)

    # Verify that the output files exist
    import os
    if os.path.exists("red_channel.png") and os.path.exists("green_channel.png") and os.path.exists("blue_channel.png"):
        print("Test passed: Output files created successfully.")
    else:
        print("Test failed: Output files not found.")

if __name__ == '__main__':
    test_Image_Channel_Extraction("./test_image.png")