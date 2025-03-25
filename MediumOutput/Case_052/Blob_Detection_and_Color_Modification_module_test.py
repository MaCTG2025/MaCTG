from Blob_Detection_and_Color_Modification import process_blobs

def test_Blob_Detection_and_Color_Modification(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Blob_Detection_and_Color_Modification module by processing an input image,
    detecting blobs, modifying the blob regions to red, and saving the modified image.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image where blobs need to be detected.
    
    output_image_path : str
        The file path where the modified image with red blobs will be saved.

    Returns:
    --------
    None
        The function does not return any value. It verifies the functionality of the module.
    """
    # Call the module function to process the image
    process_blobs(input_image_path, output_image_path)
    print(f"Test completed. Modified image saved to {output_image_path}.")

if __name__ == '__main__':
    test_Blob_Detection_and_Color_Modification("./blobs.jpg", "blobs_red.png")