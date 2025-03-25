import unittest
from rotate_image import rotate_image
import cv2
import numpy as np

class TestRotateImage(unittest.TestCase):
    def test_rotate_image(self):
        # Load an example image
        example_image_path = "./example_image.png"
        original_image = cv2.imread(example_image_path)

        # Rotate the image using the function
        rotated_image = rotate_image(example_image_path)

        # Check if the image was rotated correctly
        self.assertTrue(np.array_equal(rotated_image, cv2.rotate(original_image, cv2.ROTATE_180)))

    def test_nonexistent_image(self):
        # Test with a non-existent image path
        nonexistent_image_path = "./nonexistent_image.png"

        with self.assertRaises(ValueError):
            rotate_image(nonexistent_image_path)

    def test_invalid_image_format(self):
        # Test with an invalid image format
        invalid_image_path = "./invalid_image.txt"

        with self.assertRaises(ValueError):
            rotate_image(invalid_image_path)

if __name__ == "__main__":
    unittest.main()