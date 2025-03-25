import unittest
from load_images import load_images
import cv2
import numpy as np
import os

class TestLoadImages(unittest.TestCase):
    def setUp(self):
        # Create temporary test images
        self.background_path = "test_background.jpg"
        self.object_path = "test_object.png"
        background_img = np.zeros((100, 100, 3), dtype=np.uint8)
        object_img = np.ones((50, 50, 3), dtype=np.uint8)
        cv2.imwrite(self.background_path, background_img)
        cv2.imwrite(self.object_path, object_img)

    def tearDown(self):
        # Clean up temporary test images
        if os.path.exists(self.background_path):
            os.remove(self.background_path)
        if os.path.exists(self.object_path):
            os.remove(self.object_path)

    def test_load_images_success(self):
        background, obj = load_images(self.background_path, self.object_path)
        self.assertEqual(background.shape, (100, 100, 3))
        self.assertEqual(obj.shape, (50, 50, 3))

    def test_load_images_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_images("nonexistent_background.jpg", "nonexistent_object.png")

    def test_load_images_io_error(self):
        # Create a broken image file
        with open(self.background_path, 'w') as f:
            f.write("This is not an image file.")

        with self.assertRaises(IOError):
            load_images(self.background_path, self.object_path)

if __name__ == '__main__':
    unittest.main()