import cv2
import numpy as np

def template_matching_with_noise(
    input_image_path: str,
    template_image_path: str,
    output_image_path: str,
    sigma: float = 1.0,
    mean: float = 0.0,
    rectangle_thickness: int = 2
) -> None:
    """
    Adds Gaussian noise to the input image, performs template matching to locate the template,
    draws a red rectangle around the detected location, and saves the result.

    Args:
        input_image_path (str): Path to the input image file (e.g., "./wheres_waldo.jpg").
        template_image_path (str): Path to the template image file (e.g., "./waldo.jpg").
        output_image_path (str): Path to save the output image with the detected location (e.g., "wheres_waldo_detected.png").
        sigma (float, optional): Standard deviation of the Gaussian noise. Defaults to 1.0.
        mean (float, optional): Mean of the Gaussian noise. Defaults to 0.0.
        rectangle_thickness (int, optional): Thickness of the red rectangle to draw around the detected location. Defaults to 2.

    Returns:
        None: The function saves the output image to the specified path.

    Requirements:
        1. Add Gaussian noise to the input image using the provided sigma and mean values.
        2. Perform template matching using the method `cv2.TM_CCOEFF_NORMED`.
        3. Draw a red rectangle (BGR color: (0, 0, 255)) around the detected location with the specified thickness.
        4. Save the resulting image to the specified output path.

    Dependencies:
        - OpenCV (cv2): For image processing, template matching, and drawing.
        - NumPy (numpy): For adding Gaussian noise to the image.

    Example:
        template_matching_with_noise(
            input_image_path="./wheres_waldo.jpg",
            template_image_path="./waldo.jpg",
            output_image_path="wheres_waldo_detected.png",
            sigma=1.0,
            mean=0.0,
            rectangle_thickness=2
        )
    """
    # Load images
    input_image = cv2.imread(input_image_path)
    template_image = cv2.imread(template_image_path)

    # Check if images were loaded successfully
    if input_image is None or template_image is None:
        raise ValueError("One or both of the image paths are incorrect.")

    # Add Gaussian noise to the input image
    noise = np.random.normal(mean, sigma, input_image.shape).astype(np.uint8)
    noisy_input_image = cv2.add(input_image, noise)

    # Perform template matching
    result = cv2.matchTemplate(noisy_input_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the top-left corner of the rectangle
    top_left = max_loc

    # Calculate the width and height of the rectangle
    h, w = template_image.shape[:2]

    # Draw the rectangle on the input image
    cv2.rectangle(noisy_input_image, top_left, (top_left[0] + w, top_left[1] + h), (0, 0, 255), rectangle_thickness)

    # Save the output image
    cv2.imwrite(output_image_path, noisy_input_image)