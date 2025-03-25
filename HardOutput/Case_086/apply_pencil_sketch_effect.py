import cv2
import numpy as np

def apply_pencil_sketch_effect(input_image_path: str, output_image_path: str) -> None:
    """
    Applies a pencil sketch effect to the input image, highlights object borders, and saves the processed image to the specified output path.

    The function performs the following steps:
    1. Reads the input image from the provided path.
    2. Converts the image to grayscale.
    3. Inverts the grayscale image to create a negative effect.
    4. Applies Gaussian blur to the inverted image to smooth out details.
    5. Blends the grayscale image with the blurred inverted image to create a pencil sketch effect.
    6. Enhances object borders by applying edge detection (e.g., using Canny edge detection).
    7. Saves the final processed image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png"). The image must be in a format supported by OpenCV (e.g., PNG, JPEG).
    output_image_path : str
        The file path where the processed image will be saved (e.g., "./pencil_sketch_image.png"). The output format is determined by the file extension.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image directly to the specified output path.

    Raises:
    -------
    FileNotFoundError
        If the input image file does not exist at the specified path.
    ValueError
        If the input image cannot be read or processed (e.g., invalid file format).

    Example:
    --------
    apply_pencil_sketch_effect("./test_image.png", "./pencil_sketch_image.png")
    """
    try:
        # Read the input image
        image = cv2.imread(input_image_path)
        if image is None:
            raise ValueError("Input image cannot be read.")

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Invert the grayscale image
        inverted_gray_image = 255 - gray_image

        # Apply Gaussian blur to the inverted image
        blurred_inverted_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

        # Blend the grayscale image with the blurred inverted image
        pencil_sketch = cv2.divide(gray_image, 255 - blurred_inverted_image, scale=256)

        # Enhance object borders using Canny edge detection
        edges = cv2.Canny(pencil_sketch, 10, 70)

        # Combine the pencil sketch with the edges
        final_image = cv2.addWeighted(pencil_sketch, 0.8, edges, 0.2, 0)

        # Save the final processed image
        cv2.imwrite(output_image_path, final_image)

    except FileNotFoundError:
        raise FileNotFoundError(f"The input image file '{input_image_path}' does not exist.")
    except Exception as e:
        raise ValueError(f"An error occurred while processing the image: {str(e)}")