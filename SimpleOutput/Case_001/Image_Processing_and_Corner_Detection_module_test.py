from Image_Processing_and_Corner_Detection import process_image_and_detect_square_corners

def test_Image_Processing_and_Corner_Detection(image_path: str, output_path: str) -> None:
    """
    Tests the functionality of the Image_Processing_and_Corner_Detection module.

    Args:
        image_path (str): The file path to the input image (e.g., "./squares.jpg").
        output_path (str): The file path where the modified image will be saved.

    Returns:
        None: The function does not return any value. It tests the module by calling the function.
    """
    # Call the function to process the image and detect corners
    process_image_and_detect_square_corners(image_path, output_path)
    print(f"Test completed. Modified image saved to {output_path}.")

if __name__ == '__main__':
    test_Image_Processing_and_Corner_Detection("./squares.jpg", "squares_with_corners.png")