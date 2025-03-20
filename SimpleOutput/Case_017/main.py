from Image_Transformation import image_transformation_module

def main() -> None:
    """
    Entry point for the image transformation project.

    This function calls the image_transformation_module to perform a 180-degree rotation
    followed by a vertical flip on the input image and save the result to the specified output path.
    """
    input_image_path = "./test_image.png"
    output_image_path = "rotated_flipped_image.png"
    image_transformation_module(input_image_path, output_image_path)

if __name__ == '__main__':
    main()