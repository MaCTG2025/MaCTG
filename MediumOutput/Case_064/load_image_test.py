import unittest
from load_image import load_image
from PIL import Image
import numpy as np

class TestLoadImage(unittest.TestCase):
    def test_load_existing_image(self):
        # Assuming there is a test image named "test_image.png" in the same directory
        image_path = "./test_image.png"
        image_array = load_image(image_path)
        self.assertIsNotNone(image_array)
        self.assertIsInstance(image_array, np.ndarray)
        self.assertEqual(image_array.shape, (480, 640, 3))

    def test_load_nonexistent_image(self):
        non_existent_path = "./non_existent_image.png"
        result = load_image(non_existent_path)
        self.assertIsNone(result)

    def test_load_unsupported_format(self):
        # Assuming there is a text file named "test_text.txt" in the same directory
        unsupported_format_path = "./test_text.txt"
        result = load_image(unsupported_format_path)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()