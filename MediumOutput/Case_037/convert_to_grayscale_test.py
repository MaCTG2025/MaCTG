import unittest
from convert_to_grayscale import convert_to_grayscale
import numpy as np
import cv2

class TestConvertToGrayscale(unittest.TestCase):
    def test_grayscale_image(self):
        # Create a sample grayscale image
        image = np.zeros((100, 100), dtype=np.uint8)
        result = convert_to_grayscale(image)
        self.assertEqual(result.shape, (100, 100))
        self.assertTrue(np.all(result == 0))

    def test_bgr_image(self):
        # Create a sample BGR image
        image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
        result = convert_to_grayscale(image)
        self.assertEqual(result.shape, (100, 100))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 255))

    def test_invalid_image(self):
        # Create an invalid image with more than 3 channels
        image = np.random.randint(0, 256, size=(100, 100, 4), dtype=np.uint8)
        with self.assertRaises(cv2.error):
            convert_to_grayscale(image)

if __name__ == '__main__':
    unittest.main()