import cv2
import numpy as np

def process_image(image_path: str) -> None:
    """
    Main function that orchestrates the entire process:
    - Load the image from the specified path.
    - Apply an affine transformation (45° rotation, 1.2x scaling, and translation by (50, 30) pixels).
    - Perform Harris corner detection on both the original and transformed images.
    - Save the resulting images as "harris_original.png" and "harris_transformed.png".

    Args:
        image_path (str): The file path of the input image.

    Returns:
        None

    Requirements:
        - The image file must exist at the specified path.
        - The image must be in a format supported by OpenCV.
        - The transformation and corner detection parameters must be correctly applied.
        - The output images must be saved with the correct filenames.

    Example:
        >>> process_image("./test_image.png")
    """
    # Load the image
    img = cv2.imread(image_path)
    
    # Define the transformation matrix for 45° rotation, 1.2x scaling, and translation by (50, 30) pixels
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1.2)
    M[0, 2] += 50
    M[1, 2] += 30
    
    # Apply the affine transformation
    img_transformed = cv2.warpAffine(img, M, (cols, rows))
    
    # Convert images to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_transformed = cv2.cvtColor(img_transformed, cv2.COLOR_BGR2GRAY)
    
    # Perform Harris corner detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
    dst_transformed = cv2.cornerHarris(gray_transformed, blockSize=2, ksize=3, k=0.04)
    
    # Threshold for an optimal value, it may vary depending on the image.
    dst = cv2.dilate(dst, None)
    dst_transformed = cv2.dilate(dst_transformed, None)
    
    # Draw corners
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    img_transformed[dst_transformed > 0.01 * dst_transformed.max()] = [0, 0, 255]
    
    # Save the resulting images
    cv2.imwrite("harris_original.png", img)
    cv2.imwrite("harris_transformed.png", img_transformed)