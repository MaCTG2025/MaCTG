from PIL import Image

def transform_image(input_image_path: str, output_image_path: str) -> None:
    """
    Perform a 180-degree rotation followed by a vertical flip on the input image and save the result.

    This function takes the path to an input image, applies a 180-degree rotation and a vertical flip,
    and saves the transformed image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image that needs to be transformed. The image should be in a format
        supported by the PIL library (e.g., PNG, JPEG).

    output_image_path : str
        The file path where the transformed image will be saved. The output format will be determined
        by the file extension provided in this path.

    Returns:
    --------
    None
        The function does not return any value. The transformed image is saved directly to the specified
        output path.

    Requirements:
    -------------
    - The input image must exist at the provided `input_image_path`.
    - The output directory must exist and be writable.
    - The function uses the Python Imaging Library (PIL) via the `Pillow` package for image manipulation.

    Example:
    --------
    transform_image("./test_image.png", "rotated_flipped_image.png")
    """
    # Load the image from the input path
    with Image.open(input_image_path) as img:
        # Rotate the image 180 degrees
        rotated_img = img.rotate(180)
        # Flip the image vertically
        flipped_img = rotated_img.transpose(Image.FLIP_TOP_BOTTOM)
        # Save the transformed image to the output path
        flipped_img.save(output_image_path)