import cv2
import numpy as np

def combine_images(blurred_image: np.array, grayscale_image: np.array, binary_mask: np.array) -> np.array:
    """
    Combine the blurred bright regions with the original dark regions.

    Args:
        blurred_image (np.array): The grayscale image with Gaussian blur applied to bright regions, as a
                                 NumPy array with shape (height, width).
        grayscale_image (np.array): The original grayscale image as a NumPy array with shape (height, width).
        binary_mask (np.array): The binary mask as a NumPy array with shape (height, width), where bright
                                regions are represented by 1 (white) and dark regions by 0 (black).

    Returns:
        np.array: The final image as a NumPy array with shape (height, width), where blurred bright regions
                  are combined with the original dark regions.

    Requirements:
        - The input images and binary mask must be valid NumPy arrays with the same dimensions.
        - The function should handle mismatched dimensions gracefully.
    """
    # Check if the dimensions of the input images and binary mask match
    if blurred_image.shape != grayscale_image.shape or grayscale_image.shape != binary_mask.shape:
        raise ValueError("Input images and binary mask must have the same dimensions.")

    # Create a copy of the grayscale image to avoid modifying the original image
    final_image = grayscale_image.copy()

    # Apply the binary mask to combine the blurred bright regions with the original dark regions
    final_image[binary_mask == 1] = blurred_image[binary_mask == 1]

    return final_image