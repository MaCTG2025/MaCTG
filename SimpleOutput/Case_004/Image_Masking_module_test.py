from Image_Masking import image_masking_module

def test_Image_Masking(input_image_path: str, output_image_path: str, mask_radius: int) -> None:
    """
    Tests the functionality of the Image_Masking module by applying a circular mask to an input image.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the masked image will be saved (e.g., "masked_image.png").
    mask_radius : int
        The radius of the circular mask in pixels (e.g., 100).

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    try:
        # Call the module function
        image_masking_module(input_image_path, output_image_path, mask_radius)
        print(f"Test passed: Masked image saved successfully at {output_image_path}.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    # Test the module with sample inputs
    test_Image_Masking("./test_image.png", "masked_image.png", 100)