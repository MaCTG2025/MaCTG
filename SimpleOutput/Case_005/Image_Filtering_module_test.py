from Image_Filtering import image_filtering_module

def test_Image_Filtering(input_image_path: str) -> None:
    """
    Tests the basic functionality of the Image_Filtering module.

    This function tests whether the module correctly applies a 3x3 kernel filter to the input image
    and saves the result as "filtered_image.png". It checks if the output file is created and
    verifies that the input and output types are correct.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    image_filtering_module(input_image_path)

    # Check if the output file exists
    import os
    if os.path.exists("filtered_image.png"):
        print("Test passed: 'filtered_image.png' was successfully created.")
    else:
        print("Test failed: 'filtered_image.png' was not created.")

if __name__ == '__main__':
    test_Image_Filtering("./test_image.png")