import numpy as np
from License_Plate_Detection_and_Recognition import license_plate_detection_and_recognition

def main(image_path: str) -> tuple[np.ndarray, str]:
    """
    Main function to detect and recognize the license plate in the provided image using OCR, save the detected license plate region,
    and save the recognized text.

    Args:
        image_path (str): The file path to the input image where the license plate is to be detected.

    Returns:
        tuple[np.ndarray, str]: A tuple containing:
            - detected_plate_image (np.ndarray): The image array of the detected license plate region.
            - recognized_text (str): The text recognized from the license plate.

    Example:
        detected_plate, text = main("./dataset-card.jpg")
        print(f"Detected Plate: {detected_plate}")
        print(f"Recognized Text: {text}")
    """
    return license_plate_detection_and_recognition(image_path)

if __name__ == '__main__':
    main("./dataset-card.jpg")