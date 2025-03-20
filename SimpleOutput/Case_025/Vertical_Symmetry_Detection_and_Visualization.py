from detect_vertical_symmetry import detect_vertical_symmetry
from draw_symmetry_axis import draw_symmetry_axis
from save_image import save_image
import numpy as np

def detect_and_visualize_symmetry(image_path: str, output_path: str) -> None:
    """
    Detects vertical symmetry in an input image, visualizes the symmetry axis (if detected),
    and saves the resulting image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path where the resulting image will be saved.

    Returns:
        None
    """
    # Detect vertical symmetry
    axis_x, image = detect_vertical_symmetry(image_path)
    
    # Draw the symmetry axis (if detected)
    image_with_axis = draw_symmetry_axis(image, axis_x)
    
    # Save the resulting image
    save_image(image_with_axis, output_path)