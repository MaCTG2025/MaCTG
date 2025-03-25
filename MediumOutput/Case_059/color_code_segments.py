import numpy as np

def color_code_segments(labels: np.array, centers: np.array, image_shape: tuple) -> np.array:
    """
    Color-code the segmented regions based on the cluster labels and cluster centers.

    Args:
        labels (np.array): The cluster labels for each pixel, with shape (height * width,).
        centers (np.array): The cluster centers (mean RGB values) with shape (k, channels).
        image_shape (tuple): The original shape of the image (height, width, channels).

    Returns:
        np.array: The segmented image as a NumPy array with shape (height, width, channels).

    Raises:
        ValueError: If the input labels or centers are not valid NumPy arrays, or if the image_shape is invalid.

    Requirements:
        - Each pixel in the output image should be replaced with the RGB value of its corresponding cluster center.
        - The labels array should be reshaped back to the original image shape (height, width).
        - Ensure that the output image retains the same data type as the input image.
    """
    # Check if inputs are valid NumPy arrays
    if not isinstance(labels, np.ndarray) or not isinstance(centers, np.ndarray):
        raise ValueError("Labels and centers must be NumPy arrays.")
    
    # Check if image_shape is a valid tuple
    if not isinstance(image_shape, tuple) or len(image_shape) != 3:
        raise ValueError("Image shape must be a tuple of three integers (height, width, channels).")
    
    # Reshape labels to the original image shape
    height, width, _ = image_shape
    labels_reshaped = labels.reshape(height, width)
    
    # Create an empty image with the same shape and dtype as the input image
    segmented_image = np.zeros_like(labels_reshaped, dtype=labels.dtype)
    
    # Map each label to its corresponding center and create the segmented image
    for i in range(height):
        for j in range(width):
            segmented_image[i, j] = centers[labels_reshaped[i, j]]
    
    return segmented_image