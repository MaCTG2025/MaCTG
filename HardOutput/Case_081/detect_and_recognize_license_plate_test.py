import unittest
from detect_and_recognize_license_plate import detect_and_recognize_license_plate
import cv2
import os

class TestLicensePlateDetectionAndRecognition(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.jpg"

    def test_license_plate_detection_and_recognition(self):
        # Assuming there is a test image with a license plate named 'test_image.jpg'
        detected_plate, recognized_text = detect_and_recognize_license_plate(self.image_path)

        # Check if the detected plate image is not empty
        self.assertIsNotNone(detected_plate)

        # Check if the recognized text is not empty
        self.assertNotEqual(recognized_text, '')

        # Check if the detected plate image is saved correctly
        self.assertTrue(os.path.exists('detected_plate.png'))

        # Check if the recognized text is saved correctly
        self.assertTrue(os.path.exists('recognized_text.txt'))

if __name__ == '__main__':
    unittest.main()