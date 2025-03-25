import cv2
import numpy as np

def process_and_fill_regions(image_path: str, threshold1: int, threshold2: int, output_path: str) -> None:
    """
    Perform Canny edge detection, identify enclosed regions using contour detection, fill regions with green while preserving edges, and save the output image.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        threshold1 (int): First threshold for the hysteresis procedure in Canny edge detection (e.g., 100).
        threshold2 (int): Second threshold for the hysteresis procedure in Canny edge detection (e.g., 200).
        output_path (str): Path to save the processed image (e.g., "filled_regions.png").

    Returns:
        None: The function saves the processed image to the specified output path.

    Steps:
        1. Load the image from the provided image_path.
        2. Convert the image to grayscale.
        3. Apply Canny edge detection using the provided thresholds (threshold1 and threshold2).
        4. Use contour detection to identify enclosed regions in the image.
        5. Fill the detected regions with a solid green color (RGB: [0, 255, 0]).
        6. Ensure the edges remain visible after filling the regions.
        7. Save the final image to the specified output_path.

    Requirements:
        - The input image must be a valid image file (e.g., PNG, JPEG).
        - The output image will overwrite any existing file at the output_path.
        - The filled regions should be green (RGB: [0, 255, 0]).
        - The edges detected by Canny must remain visible in the final image.

    Dependencies:
        - OpenCV (cv2) for image processing and contour detection.
        - NumPy (numpy) for array manipulation.

    Example:
        process_and_fill_regions("./test_image.png", 100, 200, "filled_regions.png")
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, threshold1, threshold2)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a copy of the original image to draw on
    filled_image = image.copy()
    
    # Fill the regions with green
    cv2.drawContours(filled_image, contours, -1, (0, 255, 0), thickness=cv2.FILLED)
    
    # Ensure edges remain visible by XORing with the original edges
    filled_image[edges == 255] = [0, 255, 0]
    
    # Save the final image
    cv2.imwrite(output_path, filled_image)