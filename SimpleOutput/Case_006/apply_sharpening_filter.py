from PIL import Image, ImageFilter  # For image manipulation
import numpy as np                # For matrix operations
import cv2                        # For image processing

def apply_sharpening_filter(input_image_path: str, output_image_path: str) -> None:
    """
    Applies a sharpening filter to the input image and saves the result.

    The sharpening filter is a 3x3 matrix defined as:
    [[0, -1, 0],
     [-1, 5, -1],
     [0, -1, 0]]

    Args:
        input_image_path (str): The file path of the input image to be processed.
        output_image_path (str): The file path where the sharpened image will be saved.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input image file does not exist at the specified path.
        ValueError: If the input image is not a valid image format or the output path is invalid.
    """
    try:
        # Open the input image
        image = Image.open(input_image_path)
        image = np.array(image)  # Convert the image to a numpy array for processing
        
        # Apply the sharpening filter using the predefined kernel
        filter_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened_image = Image.fromarray(cv2.filter2D(image, -1, filter_kernel))
        
        # Save the sharpened image to the output path
        sharpened_image.save(output_image_path)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The input image file '{input_image_path}' does not exist.")
    except Exception as e:
        raise ValueError(f"An error occurred while processing the image: {e}")