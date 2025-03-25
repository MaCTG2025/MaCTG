import cv2
import numpy as np

def detect_and_draw_contours(rotated_image: np.array, output_path: str) -> None:
    """
    Detects contours in the rotated image, draws them in red with thickness 3, and saves the final output.

    Args:
        rotated_image (np.array): The rotated image as a NumPy array.
        output_path (str): The file path where the final image with contours will be saved.

    Returns:
        None: The function saves the final image to disk and does not return any value.

    Requirements:
        - The input image must be a valid NumPy array representing an image.
        - The function uses OpenCV to detect contours, draw them, and save the result.
        - Contours are drawn in red (BGR color: (0, 0, 255)) with a thickness of 3.
        - The output image is saved in the specified path.

    Example:
        detect_and_draw_contours(rotated_image, "rotated_contours.png")
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    cv2.drawContours(rotated_image, contours, -1, (0, 0, 255), 3)

    # Save the final image with contours
    cv2.imwrite(output_path, rotated_image)