from Image_Processing import image_processing_module

def main() -> None:
    """
    Entry point for the project. Processes an input image by converting it to grayscale, applying adaptive thresholding, and saving the binary image.

    Example:
    --------
    main()
    """
    image_processing_module("./test_image.png", "binary_image.png", blockSize=11, C=2)

if __name__ == '__main__':
    main()