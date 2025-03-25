from Blob_Detection_and_Filtering import detect_filter_and_save_blobs

def test_Blob_Detection_and_Filtering(image_path: str, min_area: int, max_area: int, output_path: str) -> None:
    """
    Tests the functionality of the Blob_Detection_and_Filtering module.

    Args:
        image_path (str): The path to the input image file.
        min_area (int): The minimum area threshold for filtering blobs.
        max_area (int): The maximum area threshold for filtering blobs.
        output_path (str): The path where the resulting image will be saved.

    Returns:
        None: The function tests the module and does not return any value.
    """
    # Call the main function of the module
    detect_filter_and_save_blobs(image_path, min_area, max_area, output_path)
    print(f"Test completed. Output saved to {output_path}.")

if __name__ == '__main__':
    # Test parameters
    image_path = "./blobs.jpg"
    min_area = 1500
    max_area = 5000
    output_path = "filtered_blobs.png"
    
    # Run the test
    test_Blob_Detection_and_Filtering(image_path, min_area, max_area, output_path)