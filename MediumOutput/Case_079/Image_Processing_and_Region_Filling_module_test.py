from Image_Processing_and_Region_Filling import image_processing_and_region_filling

def test_Image_Processing_and_Region_Filling(image_path: str, threshold1: int, threshold2: int, output_path: str) -> None:
    """
    Test the functionality of the Image_Processing_and_Region_Filling module.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        threshold1 (int): First threshold for Canny edge detection (e.g., 100).
        threshold2 (int): Second threshold for Canny edge detection (e.g., 200).
        output_path (str): Path to save the processed image (e.g., "filled_regions.png").

    Returns:
        None: The function tests the module and saves the output image.
    """
    # Call the module function
    image_processing_and_region_filling(image_path, threshold1, threshold2, output_path)
    print(f"Test completed. Output saved to {output_path}")

if __name__ == '__main__':
    test_Image_Processing_and_Region_Filling("./test_image.png", 100, 200, "filled_regions.png")