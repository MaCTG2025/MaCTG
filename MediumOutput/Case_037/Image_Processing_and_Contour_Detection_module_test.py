from Image_Processing_and_Contour_Detection import process_image

def test_Image_Processing_and_Contour_Detection(image_path: str, output_path: str) -> None:
    """
    Test the Image_Processing_and_Contour_Detection module by processing an image and saving the result.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the processed image will be saved.

    Returns:
        None
    """
    # Test the module by processing the image
    process_image(image_path, output_path)
    print(f"Image processing completed. Output saved to {output_path}")

if __name__ == '__main__':
    # Test with the provided input and output paths
    test_Image_Processing_and_Contour_Detection("./test_image.png", "adaptive_threshold_contours.png")