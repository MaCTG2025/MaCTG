import cv2
import numpy as np

def save_processed_image(image: np.array, output_path: str) -> None:
    """
    Save the processed image to the specified file path.

    Args:
        image (np.array): The processed image as a NumPy array.
        output_path (str): The file path where the processed image will be saved.

    Returns:
        None: The function saves the image to disk and does not return any value.

    Raises:
        ValueError: If the image cannot be saved (e.g., invalid file path or unsupported format).

    Notes:
        - The function uses OpenCV's `cv2.imwrite` to save the image.
        - The file format is determined by the extension in `output_path`.
        - The image is saved in BGR format by default.
    """
    try:
        cv2.imwrite(output_path, image)
    except Exception as e:
        raise ValueError(f"Failed to save image: {e}")