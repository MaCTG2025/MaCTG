import cv2
from typing import Optional

def split_and_save_rgb_channels(image_path: str) -> None:
    """
    Splits an RGB image into its three color channels (Red, Green, Blue) and saves each channel as a separate grayscale PNG file.

    Args:
        image_path (str): The file path to the input RGB image. The image should be in PNG format.

    Returns:
        None: This function does not return any value. It saves the following files directly to disk:
            - "red_channel.png": Grayscale image representing the Red channel.
            - "green_channel.png": Grayscale image representing the Green channel.
            - "blue_channel.png": Grayscale image representing the Blue channel.

    Raises:
        ValueError: If the input image is not in RGB format or the file path is invalid.
    """
    try:
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        
        # Check if the image was successfully loaded
        if image is None:
            raise ValueError("Invalid file path or the file is not an image.")
        
        # Split the image into its RGB channels
        b, g, r = cv2.split(image)
        
        # Save each channel as a grayscale PNG file
        cv2.imwrite("red_channel.png", r)
        cv2.imwrite("green_channel.png", g)
        cv2.imwrite("blue_channel.png", b)
    
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")