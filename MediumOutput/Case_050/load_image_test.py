import unittest
from load_image import load_image
from PIL import Image
import numpy as np

class TestLoadImage(unittest.TestCase):
    def test_load_valid_image(self):
        # Create a temporary image for testing
        temp_image = Image.new('RGB', (100, 100), color='red')
        temp_image.save('temp_test_image.png')

        # Test loading the valid image
        image_array = load_image('temp_test_image.png')
        self.assertIsInstance(image_array, np.ndarray)
        self.assertEqual(image_array.shape, (100, 100, 3))
        self.assertTrue(np.allclose(image_array[:, :, 0], 255))  # Red channel should be 255

    def test_load_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            load_image('nonexistent_file.png')

    def test_load_unsupported_format(self):
        with self.assertRaises(ValueError):
            load_image('temp_test_image.txt')

if __name__ == '__main__':
    unittest.main()