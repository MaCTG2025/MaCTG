from Image_Hue_Modification import process_image_hue_modification

def test_Image_Hue_Modification(image_path: str) -> None:
    """
    Tests the functionality of the Image_Hue_Modification module.

    This test function verifies that the module correctly processes an image by modifying
    its Hue channel and saving the result to disk.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    """
    # Call the module function to process the image
    process_image_hue_modification(image_path)
    print("Test completed. Check for 'hue_modified_image.png' in the current directory.")

if __name__ == '__main__':
    test_Image_Hue_Modification("./test_image.png")