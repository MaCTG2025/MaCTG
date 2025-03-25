from Dynamic_Color_Filtering import dynamic_color_filter_module

def test_Dynamic_Color_Filtering(image_path: str, brightness_threshold: int = 150) -> None:
    """
    Tests the dynamic_color_filter_module function by applying dynamic color filtering to an image
    and verifying that the output file 'filtered_image.png' is created.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.

    brightness_threshold : int, optional (default=150)
        The brightness threshold value for grayscale conversion.

    Returns:
    --------
    None
        Prints a success message if the test passes, otherwise raises an error.
    """
    # Call the module function
    dynamic_color_filter_module(image_path, brightness_threshold)

    # Verify that the output file is created
    import os
    if not os.path.exists("filtered_image.png"):
        raise FileNotFoundError("The output file 'filtered_image.png' was not created.")
    else:
        print("Test passed: 'filtered_image.png' was successfully created.")

if __name__ == '__main__':
    test_Dynamic_Color_Filtering("./test_image.png", brightness_threshold=150)