import cv2
import numpy as np

def apply_affine_transform(image: np.array) -> np.array:
    """
    Apply an affine transformation to the input image. The transformation includes:
    - 45° rotation (counter-clockwise).
    - 1.2x scaling.
    - Translation by (50, 30) pixels.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).

    Returns:
        np.array: The transformed image as a NumPy array.

    Requirements:
        - The input image must be a valid NumPy array.
        - The transformation matrix must be computed correctly.
        - The transformed image should retain the same number of channels as the input image.

    Example:
        >>> transformed_image = apply_affine_transform(image)
    """
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Compute the center of the image for translation
    center = (width // 2, height // 2)

    # Define the rotation angle, scale factor, and translation vector
    angle = 45
    scale = 1.2
    translation = (50, 30)

    # Create the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Combine the rotation matrix with the translation vector
    rotation_matrix[0, 2] += translation[0]
    rotation_matrix[1, 2] += translation[1]

    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return transformed_image