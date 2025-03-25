from Image_Processing_and_Masking import image_processing_module

def test_image_processing_module(image_path: str) -> None:
    """
    Tests the functionality of the image_processing_module by processing an input image and
    verifying that the output file "masked_image.png" is created.

    Args:
        image_path (str): The file path to the input image (e.g., "./test_image.png").

    Returns:
        None: The function does not return any value. It verifies the output file is created.
    """
    # Call the module function
    image_processing_module(image_path)

    # Verify that the output file "masked_image.png" is created
    import os
    assert os.path.exists("masked_image.png"), "Output file 'masked_image.png' was not created."

if __name__ == '__main__':
    test_image_processing_module("./test_image.png")