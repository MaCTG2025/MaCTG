import cv2
from typing import Tuple

def apply_clahe(input_image_path: str, output_image_path: str, clipLimit: float = 2.0, tileGridSize: Tuple[int, int] = (8, 8)) -> None:
    """
    Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) to the input image and saves the result.

    Args:
        input_image_path (str): The file path to the input image that needs to be processed.
        output_image_path (str): The file path where the processed image will be saved.
        clipLimit (float, optional): Threshold for contrast limiting. Defaults to 2.0.
        tileGridSize (Tuple[int, int], optional): Size of the grid for histogram equalization. Defaults to (8, 8).

    Returns:
        None: The function does not return any value. The processed image is saved to the specified output path.

    Requirements:
        1. The input image must be a valid image file (e.g., PNG, JPEG).
        2. The output path must include a valid file extension (e.g., '.png').
        3. The function uses OpenCV's CLAHE implementation, so the input image will be converted to grayscale before processing.
        4. The function handles errors such as invalid file paths or unsupported image formats by raising appropriate exceptions.

    Example:
        apply_clahe('./test_image.png', './clahe_image.png', clipLimit=2.0, tileGridSize=(8, 8))
    """
    try:
        # Read the input image
        img = cv2.imread(input_image_path)
        
        # Check if image is loaded properly
        if img is None:
            raise ValueError("Input image could not be read.")
        
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Create a CLAHE object
        clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
        
        # Apply CLAHE to the grayscale image
        clahed_img = clahe.apply(gray_img)
        
        # Save the processed image
        cv2.imwrite(output_image_path, clahed_img)
    
    except Exception as e:
        raise Exception(f"An error occurred: {e}")