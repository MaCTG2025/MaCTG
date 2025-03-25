from Image_Rotation_and_Contour_Detection import process_image_with_contours

def test_Image_Rotation_and_Contour_Detection(image_path: str, output_path: str) -> None:
    """
    Tests the functionality of the Image_Rotation_and_Contour_Detection module.

    Args:
        image_path (str): The file path to the input image.
        output_path (str): The file path where the final image with contours will be saved.

    Returns:
        None: The function tests the module and does not return any value.

    Example:
        test_Image_Rotation_and_Contour_Detection("./test_image.png", "rotated_contours.png")
    """
    # Test the process_image_with_contours function
    process_image_with_contours(image_path, output_path)
    print(f"Test completed. Output saved to {output_path}")

if __name__ == '__main__':
    test_Image_Rotation_and_Contour_Detection("./test_image.png", "rotated_contours.png")