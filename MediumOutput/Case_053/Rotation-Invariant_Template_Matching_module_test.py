import cv2
import numpy as np
from typing import List
from Rotation-Invariant_Template_Matching import rotation_invariant_template_matching

def test_rotation_invariant_template_matching(main_image_path: str, template_image_path: str, angles: List[int], rectangle_thickness: int = 2) -> np.ndarray:
    """
    Tests the rotation_invariant_template_matching function by running it with the provided inputs
    and verifying the output type and correctness.

    Args:
        main_image_path (str): The file path to the main image where the template will be searched.
        template_image_path (str): The file path to the template image to be matched.
        angles (List[int]): A list of angles (e.g., [0, 45, 90, 135]) at which the template will be rotated and matched.
        rectangle_thickness (int, optional): The thickness of the rectangle to be drawn around the matched region. Defaults to 2.

    Returns:
        np.ndarray: The resulting image with the rectangle drawn around the matched region.
    """
    # Call the function to test
    result_image = rotation_invariant_template_matching(main_image_path, template_image_path, angles, rectangle_thickness)

    # Verify the output type
    assert isinstance(result_image, np.ndarray), "Output is not a numpy array."

    # Verify the output image is not empty
    assert result_image.size > 0, "Output image is empty."

    # Display the result for visual verification
    cv2.imshow("Test Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result_image

if __name__ == '__main__':
    # Test the module with sample inputs
    main_image_path = "./wheres_waldo.jpg"
    template_image_path = "./waldo_rotate.jpg"
    angles = [0, 45, 90, 135]
    rectangle_thickness = 2

    test_rotation_invariant_template_matching(main_image_path, template_image_path, angles, rectangle_thickness)