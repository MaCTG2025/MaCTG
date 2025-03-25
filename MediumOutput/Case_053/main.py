import cv2
import numpy as np
from typing import List
from rotate_template import rotate_template
from find_and_draw_template import find_and_draw_template

def rotation_invariant_template_matching(main_image_path: str, template_image_path: str, angles: List[int], rectangle_thickness: int = 2) -> np.ndarray:
    """
    Performs rotation-invariant template matching on the main image using the template image at specified angles.
    Finds the best match, draws a rectangle around the matched region, and saves the result.

    Args:
        main_image_path (str): The file path to the main image where the template will be searched.
        template_image_path (str): The file path to the template image to be matched.
        angles (List[int]): A list of angles (e.g., [0, 45, 90, 135]) at which the template will be rotated and matched.
        rectangle_thickness (int, optional): The thickness of the rectangle to be drawn around the matched region. Defaults to 2.

    Returns:
        np.ndarray: The resulting image with the rectangle drawn around the matched region.
    """
    result_image = find_and_draw_template(main_image_path, template_image_path, angles, rectangle_thickness)
    return result_image

if __name__ == '__main__':
    rotation_invariant_template_matching("./wheres_waldo.jpg", "./waldo_rotate.jpg", [0, 45, 90, 135])