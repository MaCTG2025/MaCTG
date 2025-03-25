from detect_blobs import detect_blobs
from filter_blobs_by_area import filter_blobs_by_area
from draw_and_save_blobs import draw_and_save_blobs
import numpy as np

def detect_filter_and_save_blobs(image_path: str, min_area: int, max_area: int, output_path: str) -> None:
    """
    Detects blobs in the provided image, filters them by area, and saves the result.

    Args:
        image_path (str): The path to the input image file.
        min_area (int): The minimum area threshold for filtering blobs.
        max_area (int): The maximum area threshold for filtering blobs.
        output_path (str): The path where the resulting image will be saved.

    Returns:
        None: The function saves the image to disk and does not return any value.
    """
    blobs, image = detect_blobs(image_path)
    filtered_blobs = filter_blobs_by_area(blobs, min_area, max_area)
    draw_and_save_blobs(image, filtered_blobs, output_path)

if __name__ == '__main__':
    detect_filter_and_save_blobs('./blobs.jpg', 1500, 5000, 'filtered_blobs.png')