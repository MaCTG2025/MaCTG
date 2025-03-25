from process_image_and_detect_keypoints import process_image_and_detect_keypoints

def image_keypoint_detection_and_visualization(image_path: str) -> None:
    """
    Entry point for the Image Keypoint Detection and Visualization module.
    Processes the input image by splitting it into R, G, and B channels,
    detects keypoints using ORB, draws the keypoints in red, and saves the results.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the processed images directly to disk.

    Example:
    --------
    image_keypoint_detection_and_visualization('./test_image.png')
    """
    process_image_and_detect_keypoints(image_path)