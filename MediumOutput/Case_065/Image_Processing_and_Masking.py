from process_and_mask_image import process_and_mask_image

def image_processing_module(image_path: str) -> None:
    """
    Processes an input image by converting it to HSV, applying a circular mask to the Hue channel,
    converting it back to RGB, and saving the masked image as "masked_image.png".

    Args:
        image_path (str): The file path to the input image (e.g., "./test_image.png").

    Returns:
        None: The function does not return any value. It saves the processed image directly to disk.
    """
    process_and_mask_image(image_path)