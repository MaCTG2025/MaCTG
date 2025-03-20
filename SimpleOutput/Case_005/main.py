from Image_Filtering import image_filtering_module

def main() -> None:
    """
    Entry point for the image filtering project.
    This function calls the `image_filtering_module` to apply a 3x3 kernel filter to the input image
    and save the result as "filtered_image.png".

    Parameters:
    -----------
    None

    Returns:
    --------
    None
    """
    input_image_path = "./test_image.png"
    image_filtering_module(input_image_path)

if __name__ == '__main__':
    main()