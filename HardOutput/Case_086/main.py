from apply_pencil_sketch_effect import apply_pencil_sketch_effect

def apply_artistic_effects(input_image_path: str, output_image_path: str) -> None:
    """
    Applies artistic effects to the input image, including a pencil sketch effect with highlighted object borders,
    and saves the processed image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png"). The image must be in a format supported by OpenCV (e.g., PNG, JPEG).
    output_image_path : str
        The file path where the processed image will be saved (e.g., "./pencil_sketch_image.png"). The output format is determined by the file extension.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image directly to the specified output path.

    Example:
    --------
    apply_artistic_effects("./test_image.png", "./pencil_sketch_image.png")
    """
    apply_pencil_sketch_effect(input_image_path, output_image_path)

if __name__ == '__main__':
    apply_artistic_effects("./test_image.png", "./pencil_sketch_image.png")