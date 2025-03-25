import cv2
import numpy as np
import os

def process_and_mask_image(image_path: str) -> None:
    """
    Converts an input image from RGB to HSV, applies a circular mask with a radius of 100 pixels 
    at the center of the Hue channel, converts it back to RGB, and saves the masked image as 
    "masked_image.png".

    Args:
        image_path (str): The file path to the input image (e.g., "./test_image.png").

    Returns:
        None: The function does not return any value. It saves the processed image directly to disk 
              as "masked_image.png".
    """
    # Read the input image from the provided file path
    image = cv2.imread(image_path)

    # Convert the image from RGB to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Get the dimensions of the image
    height, width = hsv_image.shape[:2]

    # Create a circular mask with a radius of 100 pixels at the center of the Hue channel
    mask = np.zeros((height, width), dtype=np.uint8)
    center = (width // 2, height // 2)
    cv2.circle(mask, center, 100, (255), -1)

    # Apply the mask to the Hue channel
    hsv_image[mask == 255] = image[mask == 255]


    # Save the resulting image as "masked_image.png"
    cv2.imwrite("masked_image.png", hsv_image)