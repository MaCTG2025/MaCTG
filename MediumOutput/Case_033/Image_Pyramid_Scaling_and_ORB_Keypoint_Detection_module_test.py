from Image_Pyramid_Scaling_and_ORB_Keypoint_Detection import image_pyramid_scaling_and_orb_keypoint_detection

def test_Image_Pyramid_Scaling_and_ORB_Keypoint_Detection(image_path: str, nfeatures: int = 500) -> None:
    """
    Test function for the Image_Pyramid_Scaling_and_ORB_Keypoint_Detection module.

    Args:
        image_path (str): The file path to the input image.
        nfeatures (int, optional): The number of ORB keypoints to detect. Defaults to 500.

    Returns:
        None: The function calls the module function and verifies its basic functionality.
    """
    # Call the module function
    image_pyramid_scaling_and_orb_keypoint_detection(image_path, nfeatures)
    print("Test completed. Check for 'orb_upscaled.png' and 'orb_downscaled.png' in the current directory.")

if __name__ == '__main__':
    test_Image_Pyramid_Scaling_and_ORB_Keypoint_Detection("./test_image.png", nfeatures=500)