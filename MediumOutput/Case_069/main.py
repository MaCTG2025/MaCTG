from IMAGE_RESCALING_AND_CONTOUR_DETECTION import image_rescaling_and_contour_detection

def main() -> None:
    """
    Entry point for the project. Calls the image_rescaling_and_contour_detection function
    to process the input image and save the results.
    """
    image_rescaling_and_contour_detection(
        image_path="./test_image.png",
        output_path_linear="rescaled_linear.png",
        output_path_cubic="rescaled_cubic.png",
        contour_color=(0, 0, 255),
        contour_thickness=3
    )

if __name__ == '__main__':
    main()