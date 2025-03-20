from transform_image import transform_image

def image_transformation_module(input_image_path: str, output_image_path: str) -> None:
    """
    Perform a series of image transformations on the input image and save the result.

    This module-level function applies a 180-degree rotation followed by a vertical flip
    to the input image and saves the transformed image to the specified output path.

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
    """
    transform_image(input_image_path, output_image_path)