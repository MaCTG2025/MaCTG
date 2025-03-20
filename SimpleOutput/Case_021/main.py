from convert_image_to_lab import convert_image_to_lab

def image_color_space_conversion(input_image_path: str, output_image_path: str) -> None:
    """
    Converts an input image to the LAB color space and saves the resulting image to a specified file path.

    Args:
        input_image_path (str): The file path of the input image to be converted.
                               Example: "./test_image.png"
        output_image_path (str): The file path where the LAB-converted image will be saved.
                                 Example: "lab_image.png"

    Returns:
        None: The function does not return any value. It saves the LAB-converted image to disk.

    Example Usage:
        image_color_space_conversion("./test_image.png", "lab_image.png")
    """
    convert_image_to_lab(input_image_path, output_image_path)

if __name__ == '__main__':
    image_color_space_conversion("./test_image.png", "lab_image.png")