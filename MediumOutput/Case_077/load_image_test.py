import unittest
from load_image import load_image
import os
import numpy as np

class TestLoadImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.jpg"
        # Create a test image
        self.image_data = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.test_image_path, self.image_data)

    def tearDown(self):
        # Remove the test image after each test
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_load_existing_image(self):
        image = load_image(self.test_image_path)
        self.assertIsNotNone(image)
        self.assertEqual(image.shape, (100, 100, 3))
        self.assertTrue(np.array_equal(image, self.image_data))

    def test_load_nonexistent_image(self):
        non_existent_path = "non_existent_image.jpg"
        image = load_image(non_existent_path)
        self.assertIsNone(image)

    def test_load_invalid_format(self):
        invalid_format_path = "invalid_format.txt"
        with open(invalid_format_path, 'w') as f:
            f.write("This is not an image.")
        image = load_image(invalid_format_path)
        self.assertIsNone(image)
        # Clean up the invalid format file
        if os.path.exists(invalid_format_path):
            os.remove(invalid_format_path)

if __name__ == '__main__':
    unittest.main()