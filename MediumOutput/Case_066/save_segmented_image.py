import cv2
import numpy as np

def save_segmented_image(segmented_image: np.array, output_path: str) -> None:
    """
    Saves the segmented image to a specified file path.

    Parameters:
        segmented_image (np.array): A NumPy array representing the segmented image.
        output_path (str): Path where the segmented image will be saved.

    Returns:
        None

    Requirements:
        - The segmented image is saved in PNG format.
        - The function uses OpenCV's `imwrite` method to save the image.
    """
    cv2.imwrite(output_path, segmented_image)