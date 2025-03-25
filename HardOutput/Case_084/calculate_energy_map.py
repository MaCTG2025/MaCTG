import numpy as np
from scipy.ndimage import convolve

def calculate_energy_map(image: np.array) -> np.array:
    """
    Calculate the energy map of the input image. The energy map represents the importance of each pixel in the image.

    Parameters:
    -----------
    image : np.array
        A 3D array representing the input image with shape (height × width × 3) for RGB channels.

    Returns:
    --------
    energy_map : np.array
        A 2D array representing the energy map with shape (height × width). Each value in the array
        corresponds to the energy (importance) of the corresponding pixel in the input image.

    Requirements:
    -------------
    - The energy map should be computed using a gradient-based method (e.g., Sobel operator) to highlight edges
      and important features in the image.
    - The output energy map should be normalized to ensure consistency across different images.
    """
    # Convert the image from RGB to grayscale
    gray_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

    # Define the Sobel operators for horizontal and vertical gradients
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])

    # Compute the gradients in x and y directions
    grad_x = convolve(gray_image, sobel_x)
    grad_y = convolve(gray_image, sobel_y)

    # Calculate the magnitude of the gradients
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

    # Normalize the gradient magnitudes to create the energy map
    energy_map = gradient_magnitude / np.max(gradient_magnitude)

    return energy_map