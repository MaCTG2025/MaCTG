import cv2
import numpy as np

def multi_scale_template_matching(image_path: str, template_path: str, scales: list[float], output_path: str) -> None:
    """
    Perform multi-scale template matching on the input image using the provided template.

    This function scales the template to the specified scales (e.g., 0.5x, 0.75x, 1.25x, 1.5x),
    finds the best match across all scales, draws a red bounding box (thickness=3) around the
    best match, and saves the resulting image to the specified output path.

    Args:
        image_path (str): Path to the input image where the template will be searched.
        template_path (str): Path to the template image that will be matched against the input image.
        scales (list[float]): List of scaling factors to apply to the template (e.g., [0.5, 0.75, 1.25, 1.5]).
        output_path (str): Path where the resulting image with the bounding box will be saved.

    Returns:
        None: The function saves the resulting image to the specified output path.

    Requirements:
        1. The input image and template image must be valid image files (e.g., JPEG, PNG).
        2. The template image should be smaller than the input image.
        3. The scales list must contain at least one scaling factor.
        4. The output path must be writable.

    Example:
        multi_scale_template_matching(
            image_path="./wheres_waldo.jpg",
            template_path="./waldo_scaled.jpg",
            scales=[0.5, 0.75, 1.25, 1.5],
            output_path="waldo_scaled_image.png"
        )
    """
    # Load the input image and template image
    img = cv2.imread(image_path)
    template = cv2.imread(template_path)

    # Get dimensions of the template
    w, h = template.shape[:-1]

    # Initialize variables to store the best match
    best_match = None
    best_score = float('-inf')

    # Iterate over each scale
    for scale in scales:
        # Resize the template
        resized_template = cv2.resize(template, (int(w * scale), int(h * scale)))

        # Get new dimensions of the resized template
        w_resized, h_resized = resized_template.shape[:-1]

        # Perform template matching
        result = cv2.matchTemplate(img, resized_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Update the best match if this scale has a better score
        if max_val > best_score:
            best_score = max_val
            best_match = (max_loc[0], max_loc[1], w_resized, h_resized)

    # Draw a red bounding box around the best match
    x, y, w_best, h_best = best_match
    cv2.rectangle(img, (x, y), (x + w_best, y + h_best), (0, 0, 255), 3)

    # Save the resulting image
    cv2.imwrite(output_path, img)