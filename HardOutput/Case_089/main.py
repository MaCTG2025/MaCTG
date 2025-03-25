from Image_Watermarking_System import image_watermarking_system

def main() -> None:
    """
    Entry point for the image watermarking system. Calls the module-level function to embed a watermark into an image.

    This function performs the following steps:
    1. Specifies the input image path (./test_image.png).
    2. Specifies the output image path (./watermarked_image.png).
    3. Calls the image_watermarking_system function to embed the watermark and save the result.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
        The function does not return any value. The watermarked image is saved to the specified output path.
    """
    input_image_path = "./test_image.png"
    output_image_path = "./watermarked_image.png"
    image_watermarking_system(input_image_path, output_image_path)

if __name__ == '__main__':
    main()