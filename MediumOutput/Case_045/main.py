from Image_Processing_Module import image_processing_module

def main() -> None:
    """
    Entry point for the image processing project.

    This function calls the `image_processing_module` function to process the input image
    by applying arithmetic operations to specific regions and saving the result.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
    """
    image_processing_module(
        image_path="./test_image.png",
        circle_radius=100,
        addition_value=50,
        subtraction_value=100,
        output_path="final_image.png"
    )

if __name__ == '__main__':
    main()