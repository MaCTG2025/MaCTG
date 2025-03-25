import unittest
from rotate_image import rotate_image
import numpy as np
import cv2

class TestRotateImage(unittest.TestCase):
    def setUp(self):
        # Create a sample image for testing
        self.image = np.zeros((100, 100), dtype=np.uint8)
        self.image[30:70, 30:70] = 255  # Draw a white square on the black background

    def test_rotate_90_degrees(self):
        rotated_image = rotate_image(self.image, 90)
        expected_shape = (100, 100)
        self.assertEqual(rotated_image.shape, expected_shape)
        self.assertTrue(np.array_equal(rotated_image[:, ::-1], self.image))

    def test_rotate_180_degrees(self):
        rotated_image = rotate_image(self.image, 180)
        expected_shape = (100, 100)
        self.assertEqual(rotated_image.shape, expected_shape)
        self.assertTrue(np.array_equal(rotated_image[::-1, ::-1], self.image))

    def test_rotate_270_degrees(self):
        rotated_image = rotate_image(self.image, 270)
        expected_shape = (100, 100)
        self.assertEqual(rotated_image.shape, expected_shape)
        self.assertTrue(np.array_equal(rotated_image[::-1, :], self.image))

if __name__ == '__main__':
    unittest.main()