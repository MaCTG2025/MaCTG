from Image_Pyramid_Scaling_and_ORB_Keypoint_Detection import image_pyramid_scaling_and_orb_keypoint_detection

def main() -> None:
    """
    Entry point for the project. Calls the module-level function to process the image.

    Args:
        None

    Returns:
        None
    """
    image_pyramid_scaling_and_orb_keypoint_detection("./test_image.png", nfeatures=500)

if __name__ == '__main__':
    main()