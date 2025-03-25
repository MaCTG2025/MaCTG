from process_and_fill_regions import process_and_fill_regions

def image_processing_and_region_filling(image_path: str, threshold1: int, threshold2: int, output_path: str) -> None:
    """
    Perform Canny edge detection, identify enclosed regions using contour detection, fill regions with green while preserving edges, and save the output image.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        threshold1 (int): First threshold for the hysteresis procedure in Canny edge detection (e.g., 100).
        threshold2 (int): Second threshold for the hysteresis procedure in Canny edge detection (e.g., 200).
        output_path (str): Path to save the processed image (e.g., "filled_regions.png").

    Returns:
        None: The function saves the processed image to the specified output path.

    Steps:
        1. Load the image from the provided image_path.
        2. Convert the image to grayscale.
        3. Apply Canny edge detection using the provided thresholds (threshold1 and threshold2).
        4. Use contour detection to identify enclosed regions in the image.
        5. Fill the detected regions with a solid green color (RGB: [0, 255, 0]).
        6. Ensure the edges remain visible after filling the regions.
        7. Save the final image to the specified output_path.

    Example:
        image_processing_and_region_filling("./test_image.png", 100, 200, "filled_regions.png")
    """
    process_and_fill_regions(image_path, threshold1, threshold2, output_path)