import cv2
import numpy as np

def rotate_image(image: np.array, angle: float = 90) -> np.array:
    """
    Rotates an image by a specified angle (in degrees).

    Args:
        image (np.array): The input image to be rotated.
        angle (float, optional): The angle by which the image is to be rotated. Defaults to 90 degrees.

    Returns:
        np.array: The rotated image.
    """
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return rotated