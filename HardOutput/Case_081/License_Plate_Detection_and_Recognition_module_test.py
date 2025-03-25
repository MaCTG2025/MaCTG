import numpy as np
from License_Plate_Detection_and_Recognition import license_plate_detection_and_recognition

def test_license_plate_detection_and_recognition(image_path: str) -> None:
    """
    Tests the functionality of the license_plate_detection_and_recognition module.

    Args:
        image_path (str): The file path to the input image where the license plate is to be detected.
    """
    # Call the module function
    detected_plate, recognized_text = license_plate_detection_and_recognition(image_path)

    # Check output types
    assert isinstance(detected_plate, np.ndarray), "detected_plate should be a NumPy array."
    assert isinstance(recognized_text, str), "recognized_text should be a string."

    # Print results for manual verification
    print(f"Detected Plate Shape: {detected_plate.shape}")
    print(f"Recognized Text: {recognized_text}")

if __name__ == '__main__':
    test_license_plate_detection_and_recognition("./dataset-card.jpg")