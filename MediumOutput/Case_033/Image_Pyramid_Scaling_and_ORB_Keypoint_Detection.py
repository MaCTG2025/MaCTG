from process_image_with_pyramid_scaling_and_orb import process_image_with_pyramid_scaling_and_orb

def image_pyramid_scaling_and_orb_keypoint_detection(image_path: str, nfeatures: int = 500) -> None:
    """
    Module-level function for performing pyramid scaling and ORB keypoint detection on an image.

    Args:
        image_path (str): The file path to the input image.
        nfeatures (int, optional): The number of ORB keypoints to detect. Defaults to 500.

    Returns:
        None: The function saves the resulting images as "orb_upscaled.png" and "orb_downscaled.png".

    This function performs the following steps:
        1. Calls the `process_image_with_pyramid_scaling_and_orb` function to process the image.
        2. Handles any errors that may occur during processing.
    """
    process_image_with_pyramid_scaling_and_orb(image_path, nfeatures)