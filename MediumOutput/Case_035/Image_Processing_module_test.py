from Image_Processing import image_processing_module

def test_Image_Processing(image_path: str) -> None:
    """
    Tests the basic functionality of the Image_Processing module by applying Gaussian blur and Canny edge detection
    to the input image and saving the result as 'canny_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image that needs to be processed.

    Returns:
    --------
    None
        The function does not return any value. It simply calls the module function and verifies the output file is created.
    """
    # Call the module function
    image_processing_module(image_path)

    # Verify that the output file 'canny_image.png' is created
    import os
    if os.path.exists("canny_image.png"):
        print("Test passed: 'canny_image.png' was successfully created.")
    else:
        print("Test failed: 'canny_image.png' was not created.")

if __name__ == '__main__':
    test_Image_Processing("./test_image.png")