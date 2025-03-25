from apply_circular_mask_and_detect_blobs import apply_circular_mask_and_detect_blobs

def image_masking_and_blob_detection(image_path: str, radius: int, output_path: str) -> None:
    """
    Applies a circular mask to the input image, detects blobs within the masked region,
    draws the detected blobs, and saves the result to the specified output path.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./blobs.jpg").
    radius : int
        The radius of the circular mask in pixels. The mask will be centered on the image.
    output_path : str
        The file path where the resulting image with detected blobs will be saved (e.g., "masked_blobs.png").

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image directly to the output_path.
    """
    apply_circular_mask_and_detect_blobs(image_path, radius, output_path)

if __name__ == '__main__':
    image_masking_and_blob_detection("./blobs.jpg", 100, "masked_blobs.png")