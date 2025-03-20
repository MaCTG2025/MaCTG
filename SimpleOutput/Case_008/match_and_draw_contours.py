import cv2
import numpy as np

def match_and_draw_contours(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Finds the closest match of the template image in the input image, draws the contours of the match in red,
    and saves the resulting image.

    Args:
        input_image_path (str): The file path to the input image where the template will be matched.
        template_image_path (str): The file path to the template image that will be searched for in the input image.
        output_image_path (str): The file path where the resulting image with the drawn contours will be saved.

    Returns:
        None: The function does not return any value. It saves the resulting image to the specified output path.

    Requirements:
        - The input and template images must be in a format supported by OpenCV (e.g., JPEG, PNG).
        - The function uses OpenCV's template matching and contour drawing capabilities.
        - The resulting image will have the contours of the closest match drawn in red.

    Steps:
        1. Load the input and template images using OpenCV.
        2. Perform template matching to find the closest match of the template in the input image.
        3. Identify the location of the best match.
        4. Draw the contours of the matched region in red on the input image.
        5. Save the resulting image to the specified output path.

    Example:
        match_and_draw_contours("./shapestomatch.jpg", "./4star.jpg", "matched_image.png")
    """
    # Load the input and template images
    input_image = cv2.imread(input_image_path)
    template_image = cv2.imread(template_image_path)

    # Perform template matching
    result = cv2.matchTemplate(input_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the dimensions of the template
    h, w = template_image.shape[:2]

    # Extract the top-left corner of the rectangle
    top_left = max_loc

    # Draw the rectangle on the input image
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(input_image, top_left, bottom_right, (0, 0, 255), 2)

    # Save the resulting image
    cv2.imwrite(output_image_path, input_image)