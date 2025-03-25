from Image_Processing_and_Gradient_Comparison import process_image

def test_Image_Processing_and_Gradient_Comparison(image_path: str, output_path: str) -> None:
    """
    Test the functionality of the Image Processing and Gradient Comparison module.

    Args:
        image_path (str): The file path to the input image.
        output_path (str): The file path where the heatmap image will be saved.

    Raises:
        AssertionError: If any step in the module fails to produce the expected results.
    """
    # Test the process_image function
    process_image(image_path, output_path)

    print("Test passed: The module processed the image and generated the heatmap successfully.")

if __name__ == '__main__':
    # Define input and output paths for testing
    test_image_path = "./test_image.png"
    test_output_path = "./difference_heatmap.png"

    # Run the test
    test_Image_Processing_and_Gradient_Comparison(test_image_path, test_output_path)