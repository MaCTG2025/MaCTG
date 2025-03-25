from Image_Processing_Module import process_image

def test_Image_Processing_Module(image_path: str, output_path: str) -> None:
    """
    Tests the basic functionality of the Image Processing Module.
    
    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the processed image.
    
    Returns:
        None: Prints the results of the test.
    """
    # Call the process_image function
    process_image(image_path, output_path)
    
    # Print success message if no errors occur
    print("Test passed: Image processing completed successfully.")

if __name__ == '__main__':
    # Test with a sample image and output path
    test_Image_Processing_Module("./test_image.png", "./test_image_processed.png")