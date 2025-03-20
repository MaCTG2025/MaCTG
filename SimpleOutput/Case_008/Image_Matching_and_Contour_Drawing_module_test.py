from Image_Matching_and_Contour_Drawing import image_matching_and_contour_drawing

def test_image_matching_and_contour_drawing(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Tests the basic functionality of the image_matching_and_contour_drawing function.

    Args:
        input_image_path (str): Path to the input image.
        template_image_path (str): Path to the template image.
        output_image_path (str): Path to save the resulting image.

    Returns:
        None
    """
    # Call the function to test
    image_matching_and_contour_drawing(input_image_path, template_image_path, output_image_path)
    print(f"Test completed. Result saved to {output_image_path}.")

if __name__ == '__main__':
    test_image_matching_and_contour_drawing("./shapestomatch.jpg", "./4star.jpg", "matched_image.png")