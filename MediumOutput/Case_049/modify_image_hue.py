import cv2
import numpy as np

def modify_image_hue(image_path: str) -> None:
    """
    Reads an image from the specified path, converts it to the HSV color space,
    modifies the Hue channel by adding 50 (with wrapping around if necessary),
    converts it back to the RGB color space, and saves the modified image to disk.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed. The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The modified image is saved to disk as
        "hue_modified_image.png" in the current working directory.

    Requirements:
    -------------
    1. The input image must be a valid image file readable by OpenCV.
    2. The Hue channel modification should handle wrapping around (e.g., if Hue + 50 exceeds 179,
       it should wrap around to 0).
    3. The modified image should be saved in the same directory as the input image with the
       filename "hue_modified_image.png".

    Example:
    --------
    modify_image_hue("./test_image.png")
    # This will read "test_image.png", modify its Hue channel, and save the result as
    # "hue_modified_image.png".
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image from BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Modify the Hue channel by adding 50 and handling wrapping around
    hue_channel = hsv_image[:, :, 0]
    hue_channel = (hue_channel + 50) % 180
    hsv_image[:, :, 0] = hue_channel
    
    # Convert the image back from HSV to BGR
    modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    
    # Save the modified image to disk
    cv2.imwrite("hue_modified_image.png", modified_image)