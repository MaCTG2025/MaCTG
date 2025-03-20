import cv2
import numpy as np

def locate_and_draw_bounding_box(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Locates the template image within the input image, draws a red bounding box around the matched region,
    and saves the resulting image.

    Args:
        input_image_path (str): The file path to the input image where the template will be searched.
        template_image_path (str): The file path to the template image that will be searched for within the input image.
        output_image_path (str): The file path where the resulting image with the bounding box will be saved.

    Returns:
        None: The function does not return any value. It saves the resulting image to the specified output path.

    Requirements:
        1. The function uses OpenCV's template matching method (`cv2.matchTemplate`) to locate the template.
        2. The bounding box is drawn in red (BGR color: (0, 0, 255)) with a thickness of 2 pixels using `cv2.rectangle`.
        3. The resulting image is saved in the same format as the input image.
        4. The function should handle cases where the template is not found in the input image by logging an appropriate message
           and not saving any output image.

    Example:
        locate_and_draw_bounding_box("./wheres_waldo.jpg", "./waldo.jpg", "waldo_image.png")
    """
    # Load the input and template images
    input_image = cv2.imread(input_image_path)
    template_image = cv2.imread(template_image_path)

    if input_image is None or template_image is None:
        print("Error: One or both of the images could not be loaded.")
        return

    # Get dimensions of the template
    template_height, template_width = template_image.shape[:2]

    # Perform template matching
    result = cv2.matchTemplate(input_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is good enough
    threshold = 0.8
    if max_val < threshold:
        print("Warning: Template not found in the input image.")
        return

    # Get top-left corner of the rectangle
    top_left = max_loc

    # Draw the bounding box
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(input_image, top_left, bottom_right, (0, 0, 255), 2)

    # Save the resulting image
    cv2.imwrite(output_image_path, input_image)