import unittest
from load_and_validate_image import load_and_validate_image
import os
import numpy as np

class TestLoadAndValidateImage(unittest.TestCase):
    def test_valid_image(self):
        # Path to a valid image file
        image_path = "path/to/valid/image.jpg"
        
        # Check if the image exists
        self.assertTrue(os.path.exists(image_path))
        
        try:
            # Attempt to load the image
            image = load_and_validate_image(image_path)
            
            # Check if the image is loaded correctly
            self.assertIsNotNone(image)
            self.assertIsInstance(image, np.ndarray)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_nonexistent_file(self):
        # Path to a non-existent file
        image_path = "path/to/nonexistent/file.jpg"
        
        with self.assertRaises(FileNotFoundError):
            # Attempt to load the image
            load_and_validate_image(image_path)

    def test_invalid_image_format(self):
        # Path to an invalid image format (e.g., text file)
        image_path = "path/to/invalid/image.txt"
        
        with self.assertRaises(ValueError):
            # Attempt to load the image
            load_and_validate_image(image_path)

if __name__ == "__main__":
    unittest.main()