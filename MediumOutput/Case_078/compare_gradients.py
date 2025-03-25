import numpy as np

def compare_gradients(gradient_magnitude_1: np.array, gradient_magnitude_2: np.array) -> np.array:
    """
    Compare the gradient magnitudes of two images and compute the difference.

    Args:
        gradient_magnitude_1 (np.array): The gradient magnitude of the first image.
        gradient_magnitude_2 (np.array): The gradient magnitude of the second image.

    Returns:
        np.array: The difference between the two gradient magnitudes as a NumPy array.

    Raises:
        ValueError: If the input arrays are not valid NumPy arrays or have different shapes.
    """
    if not isinstance(gradient_magnitude_1, np.ndarray) or not isinstance(gradient_magnitude_2, np.ndarray):
        raise ValueError("Both inputs must be NumPy arrays.")
    
    if gradient_magnitude_1.shape != gradient_magnitude_2.shape:
        raise ValueError("Input arrays must have the same shape.")
    
    return np.abs(gradient_magnitude_1 - gradient_magnitude_2)