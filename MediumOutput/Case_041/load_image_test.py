import unittest
from load_image import load_image
import os
import numpy as np

class TestLoadImage(unittest.TestCase):
    def test_load_existing_image(self):
        # Assuming there is an existing image named 'test_image.png' in the same directory
        image_path = "test_image.png"
        self.assertTrue(os.path.exists(image_path))
        image_array = load_image(image_path)
        self.assertIsInstance(image_array, np.ndarray)
        self.assertEqual(image_array.shape, (480, 640, 3))  # Adjust the expected shape based on your test image

    def test_load_nonexistent_image(self):
        non_existent_image_path = "non_existent_image.png"
        with self.assertRaises(FileNotFoundError):
            load_image(non_existent_image_path)

if __name__ == "__main__":
    unittest.main()