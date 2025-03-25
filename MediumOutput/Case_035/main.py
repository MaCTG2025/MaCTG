from Image_Processing import image_processing_module

def main() -> None:
    """
    Entry point for the image processing project. Calls the image_processing_module function
    to apply Gaussian blur and Canny edge detection to the input image and save the result.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
    """
    image_processing_module("./test_image.png")

if __name__ == '__main__':
    main()