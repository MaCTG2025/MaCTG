from Image_Cropping import image_cropping_module

def main() -> None:
    """
    Entry point for the image cropping project.
    This function calls the `image_cropping_module` to crop the middle 75% of the input image
    and save the result to the specified output path.

    Example:
        main()
    """
    image_cropping_module("./test_image.png", "./cropped_image.png")

if __name__ == '__main__':
    main()