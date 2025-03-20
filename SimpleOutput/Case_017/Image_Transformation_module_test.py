from Image_Transformation import image_transformation_module

def test_Image_Transformation(input_image_path: str, output_image_path: str) -> None:
    """
    Test the functionality of the Image_Transformation module.

    This function tests whether the module correctly performs a 180-degree rotation
    followed by a vertical flip on the input image and saves the result to the specified
    output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image for testing.

    output_image_path : str
        The file path where the transformed image will be saved.

    Returns:
    --------
    None
    """
    # Call the module function to transform the image
    image_transformation_module(input_image_path, output_image_path)
    print(f"Transformed image saved to {output_image_path}")

if __name__ == '__main__':
    test_Image_Transformation("./test_image.png", "rotated_flipped_image.png")