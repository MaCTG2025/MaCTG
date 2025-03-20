from Image_Processing_Draw_Ellipse import process_image_with_ellipse

def main() -> None:
    """
    Entry point for the project. Processes an input image by drawing a green ellipse with fixed parameters
    and saves the result to a specified output path.

    Example:
    --------
    main()
    """
    process_image_with_ellipse("./test_image.png", "ellipse.png")

if __name__ == '__main__':
    main()