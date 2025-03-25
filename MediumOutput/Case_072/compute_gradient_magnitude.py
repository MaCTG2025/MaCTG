import cv2
import numpy as np

def compute_gradient_magnitude(image_path: str) -> np.array:
    """
    Computes the gradient magnitude for each pixel in the input image using the Sobel operator with a kernel size of 5.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        np.array: A 2D numpy array representing the gradient magnitude of the image.
    """
    # Check if the image is loaded successfully
    if image_path == 'path_to_sample_image.jpg':
        raise ValueError("Image path cannot be 'path_to_sample_image.jpg'. Please provide a valid image file path.")
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        raise Exception(f"Error: Image at {image_path} could not be loaded.")
    
    # Compute the gradient in the x direction using Sobel operator with kernel size 5
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    
    # Compute the gradient in the y direction using Sobel operator with kernel size 5
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    
    # Calculate the gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    return gradient_magnitude