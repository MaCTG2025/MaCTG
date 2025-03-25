import cv2
import numpy as np

def blend_and_save(stylized_image: np.array, edges: np.array, stylized_weight: float, edges_weight: float, output_path: str) -> None:
    """
    Blends the stylized image with the blended edges and saves the result to disk.

    Args:
        stylized_image (np.array): The stylized image as a NumPy array.
        edges (np.array): The blended edges as a NumPy array.
        stylized_weight (float): Weight for the stylized image in the blending process.
        edges_weight (float): Weight for the edges in the blending process.
        output_path (str): Path to save the final blended image.

    Returns:
        None: The function saves the final image to disk.

    Requirements:
        - The input images (stylized_image and edges) must be valid NumPy arrays.
        - The weights (stylized_weight and edges_weight) must sum to 1.0.
        - The weights must be non-negative.
        - The function uses OpenCV's addWeighted for blending and imwrite for saving the image.
    """
    # Ensure the weights sum to 1.0 and are non-negative
    assert abs(stylized_weight + edges_weight - 1.0) < 1e-6, "Weights must sum to 1.0"
    assert stylized_weight >= 0 and edges_weight >= 0, "Weights must be non-negative"

    # Blend the stylized image and edges
    if len(edges.shape) == 2 or edges.shape[2] == 1:
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    blended_image = cv2.addWeighted(stylized_image, stylized_weight, edges, edges_weight, 0)

    # Save the blended image to disk
    cv2.imwrite(output_path, blended_image)