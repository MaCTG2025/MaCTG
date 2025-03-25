import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from .utils import load_image, apply_kmeans, color_code_segments, save_image

def segment_image_using_kmeans(image_path: str, k: int, output_path: str) -> None:
    """
    A wrapper function that combines all the above steps into a single function for convenience.

    Args:
        image_path (str): The file path of the input image.
        k (int): The number of clusters to use for K-means clustering.
        output_path (str): The file path where the segmented image will be saved.

    Raises:
        FileNotFoundError: If the input image file does not exist.
        ValueError: If the input parameters are invalid (e.g., `k` is less than 1).
        IOError: If the output image cannot be saved.

    Requirements:
        - This function should call the following functions in sequence:
            1. load_image
            2. apply_kmeans
            3. color_code_segments
            4. save_image
        - Handle any errors that may occur during the process and raise exceptions instead of printing messages.
        - Ensure that the input parameters are validated before proceeding with the segmentation.
    """
    try:
        # Validate input parameters
        if k < 1:
            raise ValueError("The number of clusters 'k' must be greater than 0.")

        # Load the image
        image = load_image(image_path)

        # Apply K-means clustering
        clustered_image = apply_kmeans(image, k)

        # Color code the segments
        colored_image = color_code_segments(clustered_image)

        # Save the segmented image
        save_image(colored_image, output_path)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    except ValueError as e:
        raise ValueError(e)
    except IOError:
        raise IOError(f"Could not save the image to '{output_path}'.")