import cv2
import numpy as np

def save_image(output_image: np.array, output_path: str) -> None:
    """
    Save the resulting image to the specified file path.

    Args:
        output_image (np.array): The image to be saved as a NumPy array.
        output_path (str): The file path where the image will be saved.

    Raises:
        cv2.error: If the output image is not a valid NumPy array.
        ValueError: If the output path does not include a valid file extension (e.g., .png, .jpg).
    """
    # Check if the output image is a valid NumPy array
    if not isinstance(output_image, np.ndarray):
        raise cv2.error("The output image must be a valid NumPy array.")

    # Check if the output path includes a valid file extension
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not any(output_path.endswith(ext) for ext in valid_extensions):
        raise ValueError("The output path must include a valid file extension (e.g., .png, .jpg).")

    # Save the image using OpenCV
    cv2.imwrite(output_path, output_image)