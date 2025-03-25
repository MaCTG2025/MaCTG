from Image_Processing import image_processing_module

def main() -> None:
    """
    Entry point for the image processing project. Processes the input image by converting it to grayscale,
    applying Gaussian Blur to the upper half, and saving the result to the specified output path.

    Example Usage:
    --------------
    main()
    """
    input_image_path = "./test_image.png"
    output_image_path = "test_image_filtered.png"
    image_processing_module(input_image_path, output_image_path)

if __name__ == '__main__':
    main()