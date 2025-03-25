import numpy as np
from detect_and_recognize_license_plate import detect_and_recognize_license_plate

def license_plate_detection_and_recognition(image_path: str) -> tuple[np.ndarray, str]:
    """
    Detects and recognizes the license plate in the provided image using OCR, saves the detected license plate region,
    and saves the recognized text. This is the module-level function that encapsulates the entire process.

    Args:
        image_path (str): The file path to the input image where the license plate is to be detected.

    Returns:
        tuple[np.ndarray, str]: A tuple containing:
            - detected_plate_image (np.ndarray): The image array of the detected license plate region.
            - recognized_text (str): The text recognized from the license plate.

    Example:
        detected_plate, text = license_plate_detection_and_recognition("./dataset-card.jpg")
        print(f"Detected Plate: {detected_plate}")
        print(f"Recognized Text: {text}")
    """
    return detect_and_recognize_license_plate(image_path)