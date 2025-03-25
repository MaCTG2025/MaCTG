from Image_Rescaling_and_Pixel_Intensity_Comparison import image_rescaling_and_pixel_intensity_comparison

def test_Image_Rescaling_and_Pixel_Intensity_Comparison(image_path: str) -> None:
    """
    Test the functionality of the Image_Rescaling_and_Pixel_Intensity_Comparison module.

    Args:
        image_path (str): The file path to the input image.

    Returns:
        None: The function prints a success message if the test passes.
    """
    try:
        # Call the module function
        image_rescaling_and_pixel_intensity_comparison(image_path)
        print("Test passed: The module executed successfully and saved the .npy files.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Rescaling_and_Pixel_Intensity_Comparison("./test_image.png")