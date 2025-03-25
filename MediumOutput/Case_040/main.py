from apply_bilateral_filter import apply_bilateral_filter
from apply_multi_level_canny import apply_multi_level_canny
from blend_and_save import blend_and_save
import numpy as np

def process_image(image_path: str, output_path: str) -> None:
    """
    Processes an input image by applying bilateral filtering, multi-level Canny edge detection,
    blending the results, and saving the final output.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the final processed image.

    Returns:
        None: The function saves the final image to disk.
    """
    # Apply bilateral filtering
    filtered_image = apply_bilateral_filter(image_path, 9, 75, 75)

    # Apply multi-level Canny edge detection
    edges = apply_multi_level_canny(filtered_image, 50, 100, 150)

    # Blend the filtered image with the edges and save the result
    blend_and_save(filtered_image, edges, 0.8, 0.2, output_path)

if __name__ == '__main__':
    process_image('./test_image.png', 'bilateral_canny_image.png')