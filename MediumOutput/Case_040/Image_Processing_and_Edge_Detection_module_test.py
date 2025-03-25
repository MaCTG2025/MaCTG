from Image_Processing_and_Edge_Detection import process_image

def test_Image_Processing_and_Edge_Detection(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Image Processing and Edge Detection module.

    Args:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the final processed image.

    Returns:
        None: The function tests the module and saves the output image.
    """
    # Test the process_image function
    process_image(input_image_path, output_image_path)
    print(f"Test completed. Output saved to {output_image_path}")

if __name__ == '__main__':
    test_Image_Processing_and_Edge_Detection("./test_image.png", "bilateral_canny_image.png")