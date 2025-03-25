import cv2
import numpy as np

def process_quadrants(quadrants: dict) -> dict:
    """
    Applies specific operations to each quadrant:
        - Top-left: Gaussian Blur (kernel size=3, sigmaX=5).
        - Top-right: Sobel Edge Detection (kernel size=5).
        - Bottom-left: Image Sharpening (kernel=[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]).
        - Bottom-right: Histogram Equalization.

    Args:
        quadrants (dict): Dictionary containing the four quadrants of the image.

    Returns:
        dict: A dictionary containing the processed quadrants:
            - top_left (np.array): Processed top-left quadrant.
            - top_right (np.array): Processed top-right quadrant.
            - bottom_left (np.array): Processed bottom-left quadrant.
            - bottom_right (np.array): Processed bottom-right quadrant.

    Requirements:
        - The input quadrants must be valid NumPy arrays.
        - Gaussian Blur uses `cv2.GaussianBlur` with kernel size=3 and sigmaX=5.
        - Sobel Edge Detection uses `cv2.Sobel` with kernel size=5.
        - Image Sharpening uses a custom kernel [[0, -1, 0], [-1, 5, -1], [0, -1, 0]] with `cv2.filter2D`.
        - Histogram Equalization uses `cv2.equalizeHist`.
    """
    # Apply Gaussian Blur to the top-left quadrant
    top_left = cv2.GaussianBlur(quadrants['top_left'], (3, 3), 5)

    # Apply Sobel Edge Detection to the top-right quadrant
    top_right = cv2.Sobel(quadrants['top_right'], cv2.CV_8U, 1, 1, ksize=5)

    # Apply Image Sharpening to the bottom-left quadrant
    sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    bottom_left = cv2.filter2D(quadrants['bottom_left'], -1, sharpen_kernel)

    # Apply Histogram Equalization to the bottom-right quadrant
    bottom_right = cv2.equalizeHist(quadrants['bottom_right'])

    return {
        'top_left': top_left,
        'top_right': top_right,
        'bottom_left': bottom_left,
        'bottom_right': bottom_right
    }