import cv2
import numpy as np

def save_output_image(overlay_image: np.array, output_path: str) -> None:
    """
    Saves the final output image with the color overlay applied to a file.

    Args:
        overlay_image (np.array): A 3D numpy array representing the image with the color overlay applied.
        output_path (str): Path to save the output image file.

    Returns:
        None

    Requirements:
        - The output image should be saved in the specified path using cv2.imwrite.
        - The image format should be inferred from the file extension in the output path.
        - The function should handle any potential errors during the saving process (e.g., invalid path).
    """
    try:
        cv2.imwrite(output_path, overlay_image)
    except Exception as e:
        raise Exception(f"Error occurred while saving the image: {e}")