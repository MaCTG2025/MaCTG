from CLAHE_Image_Processing import clahe_image_processing

def test_CLAHE_Image_Processing(input_image_path: str, output_image_path: str, clipLimit: float = 2.0, tileGridSize: tuple = (8, 8)) -> None:
    """
    Tests the CLAHE_Image_Processing module by applying CLAHE to an input image and saving the result.

    Args:
        input_image_path (str): The file path to the input image that needs to be processed.
        output_image_path (str): The file path where the processed image will be saved.
        clipLimit (float, optional): Threshold for contrast limiting. Defaults to 2.0.
        tileGridSize (tuple, optional): Size of the grid for histogram equalization. Defaults to (8, 8).

    Returns:
        None: The function does not return any value. The processed image is saved to the specified output path.
    """
    clahe_image_processing(input_image_path, output_image_path, clipLimit, tileGridSize)
    print(f"CLAHE processing completed. Processed image saved to {output_image_path}")

if __name__ == '__main__':
    test_CLAHE_Image_Processing('./test_image.png', './clahe_image.png', clipLimit=2.0, tileGridSize=(8, 8))