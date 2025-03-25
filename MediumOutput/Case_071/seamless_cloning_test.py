import unittest
from seamless_cloning import seamless_cloning
import numpy as np

class TestSeamlessCloning(unittest.TestCase):
    def test_seamless_cloning(self):
        # Create a background image and an object image for testing
        bg_image = np.zeros((100, 100, 3), dtype=np.uint8)
        obj_image = np.ones((50, 50, 3), dtype=np.uint8) * 255

        result = seamless_cloning(bg_image, obj_image)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, bg_image.shape)

    def test_seamless_cloning_large_object(self):
        # Test when the object image is larger than the background image
        bg_image = np.zeros((100, 100, 3), dtype=np.uint8)
        obj_image = np.ones((150, 150, 3), dtype=np.uint8) * 255

        result = seamless_cloning(bg_image, obj_image)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, bg_image.shape)

    def test_seamless_cloning_empty_input(self):
        # Test with empty input
        bg_image = np.zeros((100, 100, 3), dtype=np.uint8)
        obj_image = np.array([])

        with self.assertRaises(ValueError):
            seamless_cloning(bg_image, obj_image)

if __name__ == '__main__':
    unittest.main()