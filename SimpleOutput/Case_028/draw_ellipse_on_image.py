import cv2
import numpy as np

def draw_ellipse_on_image(input_image_path: str, output_image_path: str) -> None:
    """
    Load an input image from the specified path, draw a green ellipse with fixed parameters, 
    and save the resulting image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. The image should be in a format 
        supported by OpenCV (e.g., PNG, JPEG).
    output_image_path : str
        The file path where the resulting image with the ellipse drawn will be saved. 
        The output format will be determined by the file extension (e.g., '.png').

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved to the specified 
        output path.

    Requirements:
    -------------
    - The ellipse is drawn with the following fixed parameters:
        - Center: (100, 100)
        - Axes: (100, 50)
        - Angle: 45 degrees
        - Thickness: 2 pixels
        - Color: Green (0, 255, 0) in BGR format.
    - The input image must exist at the specified path, and the output path must be writable.
    - The function uses OpenCV (`cv2`) for image processing.

    Example:
    --------
    draw_ellipse_on_image("./test_image.png", "ellipse.png")
    """
    # Load the input image
    image = cv2.imread(input_image_path)

    # Define the ellipse parameters
    center = (100, 100)
    axes = (100, 50)
    angle = 45
    thickness = 2
    color = (0, 255, 0)

    # Draw the ellipse on the image
    cv2.ellipse(image, center, axes, angle, 0, 360, color, thickness)

    # Save the resulting image
    cv2.imwrite(output_image_path, image)