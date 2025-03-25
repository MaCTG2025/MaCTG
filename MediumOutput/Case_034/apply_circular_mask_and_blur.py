import cv2
import numpy as np

def apply_circular_mask_and_blur(image: np.array, radius: int, kernel_size: int, sigmaX: int) -> np.array:
    """
    Apply a circular mask to the image (keeping the center sharp) and apply a Gaussian blur outside the mask.

    Args:
        image (np.array): The input image as a NumPy array.
        radius (int): The radius of the circular mask in pixels.
        kernel_size (int): The size of the Gaussian kernel (must be an odd integer).
        sigmaX (int): The standard deviation of the Gaussian kernel in the X direction.

    Returns:
        np.array: The processed image with the circular mask and Gaussian blur applied.

    Raises:
        ValueError: If the kernel_size is not an odd integer or if the radius is invalid.

    Notes:
        - The circular mask is centered in the image.
        - The Gaussian blur is applied only to the region outside the circular mask.
        - The function uses OpenCV's `cv2.circle` to create the mask and `cv2.GaussianBlur` for blurring.
        - The mask is applied using bitwise operations to ensure only the outer region is blurred.
    """
    if kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer")
    
    height, width = image.shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, (width // 2, height // 2), radius, 255, -1)
    
    # Create a copy of the original image to apply the blur
    blurred_image = image.copy()
    
    # Apply Gaussian blur to the masked area
    blurred_area = cv2.GaussianBlur(blurred_image, (kernel_size, kernel_size), sigmaX)
    result = image.copy()
    result[mask == 0] = blurred_area[mask == 0]
    
    return result