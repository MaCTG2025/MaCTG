import cv2
import numpy as np
import easyocr

def detect_and_recognize_license_plate(image_path: str) -> tuple[np.ndarray, str]:
    """
    Detects the license plate region in the provided image, recognizes the text on the detected license plate using OCR,
    saves the detected license plate region as 'detected_plate.png', and saves the recognized text as 'recognized_text.txt'.

    Args:
        image_path (str): The file path to the input image where the license plate is to be detected.

    Returns:
        tuple[np.ndarray, str]: A tuple containing:
            - detected_plate_image (np.ndarray): The image array of the detected license plate region.
            - recognized_text (str): The text recognized from the license plate.

    Requirements:
        1. Use OpenCV (cv2) for image processing and region detection.
        2. Use EasyOCR for Optical Character Recognition (OCR) to extract text from the detected license plate region.
        3. Save the detected license plate region as 'detected_plate.png'.
        4. Save the recognized text as 'recognized_text.txt'.
        5. Handle potential errors gracefully, such as no license plate being detected or OCR failing to recognize text.

    Example:
        detected_plate, text = detect_and_recognize_license_plate("./dataset-card.jpg")
        print(f"Detected Plate: {detected_plate}")
        print(f"Recognized Text: {text}")
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found at the specified path.")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over all contours
    for contour in contours:
        # Approximate the contour
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the contour has four points (i.e., a quadrilateral)
        if len(approx) == 4:
            # Calculate the bounding box of the contour
            x, y, w, h = cv2.boundingRect(approx)

            # Aspect ratio check to filter out non-rectangular shapes
            aspect_ratio = float(w) / h
            if 2 <= aspect_ratio <= 6:
                # Extract the license plate region
                license_plate_region = image[y:y+h, x:x+w]

                # Save the detected license plate region
                cv2.imwrite('detected_plate.png', license_plate_region)

                # Initialize EasyOCR reader
                reader = easyocr.Reader(['en'])

                # Perform OCR on the license plate region
                result = reader.readtext(license_plate_region)

                # Extract the recognized text
                recognized_text = ''
                for detection in result:
                    recognized_text += detection[1] + ' '

                # Save the recognized text
                with open('recognized_text.txt', 'w') as f:
                    f.write(recognized_text.strip())

                return license_plate_region, recognized_text.strip()

    # If no license plate is detected
    raise ValueError("No license plate detected in the image.")