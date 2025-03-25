import numpy as np
import cv2

def detect_corners_and_save(image: np.ndarray, output_path: str) -> None:
    """
    Detects corners in an image using Harris corner detection and saves the resulting image.

    Args:
        image (np.ndarray): The input image as a NumPy array. It must be grayscale (single-channel).
        output_path (str): The file path where the resulting image with detected corners will be saved.

    Returns:
        None

    Requirements:
        - The input image must be a valid grayscale NumPy array.
        - The output path must be a valid file path with a supported image format (e.g., .png, .jpg).
        - The function should only handle grayscale images.
    """
    # Ensure the image is grayscale
    if len(image.shape) != 2:
        raise ValueError("Input image must be grayscale.")

    # Convert grayscale image to 3-channel image
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Apply Harris corner detection
    gray = np.float32(image)
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Threshold for an optimal value, it may vary depending on the image.
    dst = cv2.dilate(dst, None)
    image_color[dst > 0.01 * dst.max()] = [0, 0, 255]

    # Save the resulting image
    cv2.imwrite(output_path, image_color)