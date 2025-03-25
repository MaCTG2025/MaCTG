import cv2
import numpy as np
from typing import List

def find_and_draw_template(main_image_path: str, template_image_path: str, angles: List[int], rectangle_thickness: int = 2) -> np.ndarray:
    """
    Performs rotation-invariant template matching by testing the template image at specified angles,
    finds the best match, draws a rectangle around the matched region, and returns the result.

    Args:
        main_image_path (str): The file path to the main image where the template will be searched.
        template_image_path (str): The file path to the template image to be matched.
        angles (List[int]): A list of angles (e.g., [0, 45, 90, 135]) at which the template will be rotated and matched.
        rectangle_thickness (int, optional): The thickness of the rectangle to be drawn around the matched region. Defaults to 2.

    Returns:
        np.ndarray: The resulting image with the rectangle drawn around the matched region.
    """
    def rotate_template(template, angle):
        (h, w) = template.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(template, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    main_image = cv2.imread(main_image_path, 0)
    template_image = cv2.imread(template_image_path, 0)

    best_match_score = -1
    best_match_location = None

    for angle in angles:
        rotated_template = rotate_template(template_image, angle)
        result = cv2.matchTemplate(main_image, rotated_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val > best_match_score:
            best_match_score = max_val
            best_match_location = max_loc

    top_left = best_match_location
    h, w = template_image.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    result_image = cv2.imread(main_image_path)
    cv2.rectangle(result_image, top_left, bottom_right, (0, 255, 0), rectangle_thickness)

    cv2.imwrite("wheres_waldo_found.png", result_image)
    return result_image