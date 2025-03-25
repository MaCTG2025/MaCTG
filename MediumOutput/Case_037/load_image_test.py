import unittest
from load_image import load_image
import os
import numpy as np
import cv2

class TestLoadImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.jpg"
        # Create a test image
        self.image_array = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.test_image_path, self.image_array)

    def tearDown(self):
        # Remove the test image after each test
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_load_existing_image(self):
        image = load_image(self.test_image_path)
        self.assertIsNotNone(image)
        self.assertEqual(image.shape, (100, 100, 3))

    def test_load_nonexistent_image(self):
        with self.assertRaises(FileNotFoundError):
            load_image("nonexistent_image.jpg")

    def test_load_invalid_format(self):
        invalid_image_path = "invalid_image.txt"
        with open(invalid_image_path, 'w') as f:
            f.write("This is not an image.")
        with self.assertRaises(cv2.error):
            load_image(invalid_image_path)
        os.remove(invalid_image_path)

if __name__ == '__main__':
    unittest.main()