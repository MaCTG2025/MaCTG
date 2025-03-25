from rotate_image import rotate_image
from detect_and_draw_contours import detect_and_draw_contours

def process_image_with_contours(image_path: str, output_path: str) -> None:
    """
    Processes an image by rotating it 180 degrees, detecting and drawing contours, and saving the result.

    Args:
        image_path (str): The file path to the input image.
        output_path (str): The file path where the final image with contours will be saved.

    Returns:
        None: The function saves the final image to disk and does not return any value.

    Example:
        process_image_with_contours("./test_image.png", "rotated_contours.png")
    """
    rotated_image = rotate_image(image_path)
    detect_and_draw_contours(rotated_image, output_path)