import cv2
import numpy as np

def process_image_and_detect_corners(image_path: str, output_path: str = "squares_with_corners.png") -> None:
    """
    Processes the input image to detect corners of squares, draws red circles on the detected corners,
    and saves the modified image to the specified output path.

    Args:
        image_path (str): The file path to the input image (e.g., "./squares.jpg").
        output_path (str, optional): The file path where the modified image will be saved. 
                                     Defaults to "squares_with_corners.png".

    Returns:
        None: The function does not return any value. It saves the modified image to the specified output path.

    Requirements:
        1. The input image should be in a format supported by OpenCV (e.g., JPEG, PNG).
        2. The function uses the Harris corner detection method to identify corners in the image.
        3. Detected corners are marked with red circles of radius 3 pixels.
        4. The modified image is saved in the same format as the input image.

    Example:
        process_image_and_detect_corners("./squares.jpg", "output_image.png")
        # This will process "squares.jpg", detect corners, draw red circles, and save the result as "output_image.png".
    """
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve corner detection
    gray_blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Detect corners using Harris Corner Detection
    dst = cv2.cornerHarris(gray_blurred, blockSize=2, ksize=3, k=0.04)
    
    # Dilate the corner points to make them more visible
    dst = cv2.dilate(dst, None)
    
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    
    # Save the image with detected corners
    cv2.imwrite(output_path, img)