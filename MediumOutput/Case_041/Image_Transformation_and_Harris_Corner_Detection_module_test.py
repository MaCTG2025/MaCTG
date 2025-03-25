from Image_Transformation_and_Harris_Corner_Detection import process_image

def test_Image_Transformation_and_Harris_Corner_Detection(image_path: str) -> None:
    """
    Test the functionality of the Image Transformation and Harris Corner Detection module.

    Args:
        image_path (str): The file path of the input image.

    Returns:
        None

    Example:
        >>> test_Image_Transformation_and_Harris_Corner_Detection("./test_image.png")
    """
    # Test the process_image function
    process_image(image_path)
    print("Test completed. Check the output images: 'harris_original.png' and 'harris_transformed.png'.")

if __name__ == '__main__':
    test_Image_Transformation_and_Harris_Corner_Detection("./test_image.png")