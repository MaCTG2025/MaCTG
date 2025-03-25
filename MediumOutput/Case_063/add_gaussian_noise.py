import numpy as np
import cv2

def add_gaussian_noise(image: np.ndarray, mean: float, std_dev: float) -> np.ndarray:
    """
    Adds Gaussian noise to an input image with a specified mean and standard deviation.

    Args:
        image (np.ndarray): The input image as a NumPy array. It can be grayscale or color (3-channel).
        mean (float): The mean of the Gaussian noise distribution.
        std_dev (float): The standard deviation of the Gaussian noise distribution.

    Returns:
        np.ndarray: The noisy image as a NumPy array with the same shape as the input image.
    """
    # Ensure the image is in the correct range for adding noise
    if image.dtype == np.uint8:
        image = image.astype(np.float64)
    
    # Generate Gaussian noise
    gaussian_noise = np.random.normal(mean, std_dev, image.shape).astype(np.float64)
    
    # Add noise to the image
    noisy_image = image + gaussian_noise
    
    # Clip the values to ensure they remain within the valid range
    if image.dtype == np.uint8:
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    return noisy_image