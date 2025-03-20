from Image_Masking import image_masking_module

def main() -> None:
    """
    Entry point for the image masking project.
    Calls the `image_masking_module` function to apply a circular mask to an input image and save the result.

    Example:
    --------
    main()
    """
    image_masking_module("./test_image.png", "masked_image.png", 100)

if __name__ == '__main__':
    main()