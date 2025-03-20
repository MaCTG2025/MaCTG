from Image_Processing_and_Corner_Detection import process_image_and_detect_square_corners

def main() -> None:
    """
    Entry point for the project. Processes the input image to detect corners of squares,
    draws red circles on the detected corners, and saves the modified image.
    """
    process_image_and_detect_square_corners("./squares.jpg", "squares_with_corners.png")

if __name__ == '__main__':
    main()