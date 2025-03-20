from Image_Processing_Draw_Ellipse import process_image_with_ellipse

def test_Image_Processing_Draw_Ellipse(input_image_path: str, output_image_path: str) -> None:
    """
    Test the functionality of the Image_Processing_Draw_Ellipse module by drawing a green ellipse
    on an input image and saving the result.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the resulting image with the ellipse drawn will be saved.

    Returns:
    --------
    None
        The function does not return any value. It verifies that the image processing works as expected.
    """
    # Call the function to process the image
    process_image_with_ellipse(input_image_path, output_image_path)
    print(f"Test completed. Output image saved to {output_image_path}.")

if __name__ == '__main__':
    test_Image_Processing_Draw_Ellipse("./test_image.png", "ellipse.png")