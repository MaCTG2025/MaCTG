import unittest
from load_image import load_image
from PIL import Image
import numpy as np
import os

class TestLoadImage(unittest.TestCase):
    def setUp(self):
        # Create a temporary image for testing
        self.temp_image_path = 'temp_test_image.png'
        self.image = Image.new('RGB', (100, 100), color='red')
        self.image.save(self.temp_image_path)

    def tearDown(self):
        # Remove the temporary image after tests
        if os.path.exists(self.temp_image_path):
            os.remove(self.temp_image_path)

    def test_load_existing_image(self):
        image_array = load_image(self.temp_image_path)
        self.assertIsInstance(image_array, np.ndarray)
        self.assertEqual(image_array.shape, (100, 100, 3))
        self.assertTrue(np.array_equal(image_array, np.full((100, 100, 3), [255, 0, 0])))

    def test_load_nonexistent_image(self):
        with self.assertRaises(FileNotFoundError):
            load_image('nonexistent_image.png')

    def test_load_corrupted_image(self):
        # Corrupt the image by writing random bytes
        with open(self.temp_image_path, 'wb') as f:
            f.write(os.urandom(100))
        
        with self.assertRaises(ValueError):
            load_image(self.temp_image_path)

if __name__ == '__main__':
    unittest.main()