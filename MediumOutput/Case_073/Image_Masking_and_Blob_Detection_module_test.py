from Image_Masking_and_Blob_Detection import image_masking_and_blob_detection

def test_image_masking_and_blob_detection(image_path: str, radius: int, output_path: str) -> None:
    """
    Tests the basic functionality of the image_masking_and_blob_detection module.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./blobs.jpg").
    radius : int
        The radius of the circular mask in pixels. The mask will be centered on the image.
    output_path : str
        The file path where the resulting image with detected blobs will be saved (e.g., "masked_blobs.png").

    Returns:
    --------
    None
        The function does not return any value. It tests the module by calling the function and verifying the output file is created.
    """
    # Call the function to test
    image_masking_and_blob_detection(image_path, radius, output_path)

    # Verify the output file is created
    import os
    if os.path.exists(output_path):
        print(f"Test passed: Output file '{output_path}' was created successfully.")
    else:
        print(f"Test failed: Output file '{output_path}' was not created.")

if __name__ == '__main__':
    test_image_masking_and_blob_detection("./blobs.jpg", 100, "masked_blobs.png")