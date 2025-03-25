import unittest
from load_image import load_image
import os
import numpy as np

class TestLoadImage(unittest.TestCase):
    def test_load_valid_image(self):
        # Create a temporary valid image file
        temp_image_path = 'temp_image.jpg'
        cv2.imwrite(temp_image_path, np.zeros((100, 100, 3), dtype=np.uint8)

        # Test loading the valid image
        image = load_image(temp_image_path)
        self.assertIsNotNone(image)
        self.assertEqual(image.shape, (100, 100, 3))

        # Clean up the temporary image file
        os.remove(temp_image_path)

    def test_load_nonexistent_image(self):
        # Test loading a non-existent image
        nonexistent_image_path = 'nonexistent_image.jpg'
        with self.assertRaises(FileNotFoundError):
            load_image(nonexistent_image_path)

    def test_load_invalid_format(self):
        # Create a temporary invalid image file
        temp_image_path = 'temp_image.txt'
        with open(temp_image_path, 'w') as f:
            f.write('This is not an image')

        # Test loading the invalid image
        with self.assertRaises(ValueError):
            load_image(temp_image_path)

        # Clean up the temporary image file
        os.remove(temp_image_path)

if __name__ == '__main__':
    unittest.main()