from typing import List
from process_and_transform_image import process_and_transform_image

def image_processing_module(image_path: str, output_points: List[List[int]]) -> None:
    """
    This module-level function processes an image by cropping its central 75% and applying a perspective transformation.
    The transformed image is saved as "perspective_transformed_image.png".

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        output_points (List[List[int]]): A list of 4 output points for the perspective transformation.
            Each point is a list of two integers representing the x and y coordinates.
            Example: [[10, 100], [10, 250], [300, 300], [300, 200]].

    Output:
        None: The function saves the transformed image to disk as "perspective_transformed_image.png".
    """
    process_and_transform_image(image_path, output_points)