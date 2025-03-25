from PIL import Image
import numpy as np
import cv2

def apply_oil_painting_effect(input_image_path: str, output_image_path: str) -> None:
    """
    Applies an oil painting effect to the input image and saves the processed image to the specified output path.

    Parameters:
        input_image_path (str): The file path of the input image to which the oil painting effect will be applied.
        output_image_path (str): The file path where the processed image will be saved.

    Returns:
        None
    """
    # Open the input image
    image = Image.open(input_image_path)
    image = np.array(image)

    # Define the kernel size
    kernel_size = 5

    # Apply the oil painting effect, using xphoto.oilPainting function
    output_image = cv2.xphoto.oilPainting(image, kernel_size, 1)

    # Save the processed image
    Image.fromarray(output_image).save(output_image_path)
