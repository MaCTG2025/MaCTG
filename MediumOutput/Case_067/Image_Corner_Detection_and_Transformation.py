from detect_and_draw_corners import detect_and_draw_corners
from rotate_image import rotate_image
from save_image import save_image
import numpy as np
import cv2

def process_image(image_path: str) -> None:
    """
    Processes an image by detecting and drawing corners, rotating it, and saving the results.

    Args:
        image_path (str): The file path of the input image to be processed.

    Returns:
        None: The processed images are saved to disk as "original_image.png" and "rotated_image_back.png".
    """
    # Load the image
    image = cv2.imread(image_path)

    # Detect and draw corners on the original image
    image_with_corners = detect_and_draw_corners(image)

    # Save the original image with corners
    save_image(image_with_corners, "original_image.png")

    # Rotate the image by 90 degrees
    rotated_image = rotate_image(image_with_corners, 90)

    # Detect and draw corners on the rotated image
    rotated_image_with_corners = detect_and_draw_corners(rotated_image)

    # Rotate the image back to its original orientation
    rotated_back_image = rotate_image(rotated_image_with_corners, -90)

    # Save the rotated back image
    save_image(rotated_back_image, "rotated_image_back.png")