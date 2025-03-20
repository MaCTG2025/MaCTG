from Morphological_Gradient_Operation import apply_morphological_gradient_module

def test_Morphological_Gradient_Operation(input_image_path: str) -> None:
    """
    Tests the functionality of the apply_morphological_gradient_module function.
    Ensures that the function processes the input image and saves the result as 'morphological_gradient.png'.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").

    Returns:
    --------
    None
        The function does not return any value. It simply tests the module functionality.
    """
    # Call the module function to process the image
    apply_morphological_gradient_module(input_image_path)
    print("Test completed. Check for 'morphological_gradient.png' in the current working directory.")

if __name__ == '__main__':
    test_Morphological_Gradient_Operation("./test_image.png")