import numpy as np

def create_binary_mask(gradient_magnitude: np.array, threshold: int = 50) -> np.array:
    """
    Creates a binary mask where gradient values exceed a specified threshold.

    Args:
        gradient_magnitude (np.array): A 2D numpy array representing the gradient magnitude of the image.
        threshold (int): The threshold value for creating the binary mask. Default is 50.

    Returns:
        np.array: A 2D numpy array representing the binary mask, where values above the threshold are set to 1,
                 and values below or equal to the threshold are set to 0.
    """
    # Create a binary mask by comparing each pixel's gradient magnitude to the threshold
    binary_mask = (gradient_magnitude > threshold).astype(int)
    
    return binary_mask