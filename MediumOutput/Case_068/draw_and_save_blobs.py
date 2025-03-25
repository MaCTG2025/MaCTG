import cv2
import numpy as np

def draw_and_save_blobs(image: np.ndarray, filtered_blobs: list[tuple[int, int, int]], output_path: str) -> None:
    """
    Draws the filtered blobs on the image and saves the result.

    Args:
        image (np.ndarray): The image as a NumPy array.
        filtered_blobs (list of tuples): A list of filtered blobs, where each blob is represented as a tuple 
                                         containing its centroid coordinates (x, y) and its area (area).
        output_path (str): The path where the resulting image will be saved.

    Returns:
        None: The function saves the image to disk and does not return any value.
    """
    for blob in filtered_blobs:
        x, y, _ = blob
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    
    cv2.imwrite(output_path, image)