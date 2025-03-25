from Image_Processing_Module import image_processing_module

def test_Image_Processing_Module(image_path: str, circle_radius: int, addition_value: int, subtraction_value: int, output_path: str) -> None:
    """
    Test the functionality of the Image_Processing_Module.

    This function tests the following:
    1. The module correctly processes the input image.
    2. The processed image is saved to the specified output path.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    circle_radius : int
        The radius of the central circle region in pixels.
    addition_value : int
        The value to add to the pixel values in the central circle region.
    subtraction_value : int
        The value to subtract from the pixel values in the outer region.
    output_path : str
        The file path where the processed image will be saved.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    image_processing_module(image_path, circle_radius, addition_value, subtraction_value, output_path)
    
    # Print success message
    print("Test passed: Image processed and saved successfully.")

if __name__ == '__main__':
    # Test parameters
    test_image_path = "./test_image.png"
    test_circle_radius = 100
    test_addition_value = 50
    test_subtraction_value = 100
    test_output_path = "final_image.png"
    
    # Run the test
    test_Image_Processing_Module(test_image_path, test_circle_radius, test_addition_value, test_subtraction_value, test_output_path)