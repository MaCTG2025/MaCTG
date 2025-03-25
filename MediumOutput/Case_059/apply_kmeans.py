import numpy as np
from sklearn.cluster import KMeans

def apply_kmeans(image: np.array, k: int) -> tuple[np.array, np.array]:
    """
    Apply K-means clustering to the image pixel values to segment the image into distinct color regions.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).
        k (int): The number of clusters to use for K-means clustering.

    Returns:
        tuple[np.array, np.array]: A tuple containing:
            - labels (np.array): The cluster labels for each pixel, with shape (height * width,).
            - centers (np.array): The cluster centers (mean RGB values) with shape (k, channels).

    Raises:
        ValueError: If the input image is not a valid NumPy array or if `k` is less than 1.

    Requirements:
        - The input image should be reshaped into a 2D array (height * width, channels) before applying K-means.
        - Use the sklearn.cluster.KMeans implementation for clustering.
        - Ensure that the number of clusters `k` is valid and does not exceed the number of unique pixel values.
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("Input image must be a NumPy array.")
    if k < 1:
        raise ValueError("Number of clusters 'k' must be at least 1.")

    # Reshape the image to a 2D array where each row represents a pixel's RGB values
    pixels = image.reshape(-1, image.shape[-1])

    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit_predict(pixels)
    centers = kmeans.cluster_centers_

    return labels, centers