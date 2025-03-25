import cv2
import numpy as np

def filter_blobs_by_area(blobs: list[tuple[int, int, int]], min_area: int, max_area: int) -> list[tuple[int, int, int]]:
    """
    Filters the detected blobs based on the specified area range.

    Args:
        blobs (list of tuples): A list of detected blobs, where each blob is represented as a tuple 
                                containing its centroid coordinates (x, y) and its area (area).
        min_area (int): The minimum area threshold for filtering blobs.
        max_area (int): The maximum area threshold for filtering blobs.

    Returns:
        filtered_blobs (list of tuples): A list of blobs that fall within the specified area range.
    """
    filtered_blobs = [blob for blob in blobs if min_area <= blob[2] <= max_area]
    return filtered_blobs