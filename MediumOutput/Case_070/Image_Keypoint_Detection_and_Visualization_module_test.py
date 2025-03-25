from Image_Keypoint_Detection_and_Visualization import image_keypoint_detection_and_visualization

def test_image_keypoint_detection_and_visualization(image_path: str) -> None:
    """
    Tests the basic functionality of the Image Keypoint Detection and Visualization module.
    Ensures that the module processes the input image, detects keypoints, and saves the results.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It simply calls the module function and verifies its execution.
    """
    # Call the module function
    image_keypoint_detection_and_visualization(image_path)
    print("Test completed. Check the output files: 'keypoints_R.png', 'keypoints_G.png', 'keypoints_B.png'.")

if __name__ == '__main__':
    test_image_keypoint_detection_and_visualization('./test_image.png')