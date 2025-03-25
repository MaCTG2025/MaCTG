from IMAGE_RESCALING_AND_CONTOUR_DETECTION import image_rescaling_and_contour_detection

def test_IMAGE_RESCALING_AND_CONTOUR_DETECTION() -> None:
    """
    Test the functionality of the IMAGE_RESCALING_AND_CONTOUR_DETECTION module.
    """
    # Define input and output paths
    image_path = "./test_image.png"
    output_path_linear = "rescaled_linear.png"
    output_path_cubic = "rescaled_cubic.png"

    # Call the module function
    image_rescaling_and_contour_detection(
        image_path=image_path,
        output_path_linear=output_path_linear,
        output_path_cubic=output_path_cubic,
        contour_color=(255, 0, 0),
        contour_thickness=3
    )

    # Print success message if no errors occur
    print("Test passed: Images rescaled and saved successfully.")

if __name__ == '__main__':
    test_IMAGE_RESCALING_AND_CONTOUR_DETECTION()