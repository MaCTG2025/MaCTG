import cv2
import numpy as np

def apply_multi_level_canny(image: np.array, low_threshold: int, medium_threshold: int, high_threshold: int) -> np.array:
    """
    Applies multi-level Canny edge detection to the input image and blends the edges.

    Args:
        image (np.array): Input image as a NumPy array.
        low_threshold (int): Lower threshold for Canny edge detection.
        medium_threshold (int): Medium threshold for Canny edge detection.
        high_threshold (int): Higher threshold for Canny edge detection.

    Returns:
        np.array: A blended edge map as a NumPy array.
    """
    # Apply Canny edge detection at three levels
    edges_low = cv2.Canny(image, low_threshold, medium_threshold)
    edges_medium = cv2.Canny(image, medium_threshold, high_threshold)
    edges_high = cv2.Canny(image, high_threshold, high_threshold * 2)

    # Blend the edge maps by averaging
    blended_edges = (edges_low * 0.3 + edges_medium * 0.3 + edges_high * 0.4).astype(np.uint8)

    return blended_edges