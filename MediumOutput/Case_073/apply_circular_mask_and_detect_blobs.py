import cv2
import numpy as np

def apply_circular_mask_and_detect_blobs(image_path: str, radius: int, output_path: str) -> None:
    """
    Applies a circular mask to the input image, detects blobs within the masked region, 
    draws the detected blobs, and saves the result to the specified output path.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./blobs.jpg").
    radius : int
        The radius of the circular mask in pixels. The mask will be centered on the image.
    output_path : str
        The file path where the resulting image with detected blobs will be saved (e.g., "masked_blobs.png").

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image directly to the output_path.

    Requirements:
    -------------
    1. The input image must be a valid image file (e.g., JPEG, PNG).
    2. The circular mask will be centered on the image.
    3. Blobs are detected only within the masked region using a blob detection algorithm.
    4. Detected blobs are drawn on the image using `cv2.drawKeypoints`.
    5. The resulting image is saved to the specified output path.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing and blob detection.
    - NumPy (numpy) for array operations.

    Example:
    --------
    apply_circular_mask_and_detect_blobs("./blobs.jpg", 100, "masked_blobs.png")
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Create a mask with the same size as the image
    mask = np.zeros_like(image)
    
    # Get the center of the image
    center = (image.shape[1] // 2, image.shape[0] // 2)
    
    # Draw a circle on the mask
    cv2.circle(mask, center, radius, (255, 255, 255), -1)
    
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, mask)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
    
    # Detect blobs
    params = cv2.SimpleBlobDetector_Params()
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(gray)
    
    # Draw the keypoints on the original image
    result_image = cv2.drawKeypoints(image, keypoints, None, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Save the result
    cv2.imwrite(output_path, result_image)