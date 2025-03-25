import unittest
from save_processed_image import save_processed_image
import numpy as np
import os

class TestSaveProcessedImage(unittest.TestCase):
    def setUp(self):
        self.test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.output_path = "test_output.png"

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_save_png_image(self):
        save_processed_image(self.test_image, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_save_jpg_image(self):
        jpg_output_path = "test_output.jpg"
        save_processed_image(self.test_image, jpg_output_path)
        self.assertTrue(os.path.exists(jpg_output_path))
        os.remove(jpg_output_path)

    def test_invalid_file_path(self):
        with self.assertRaises(ValueError):
            save_processed_image(self.test_image, "/invalid/path/to/image.txt")

if __name__ == "__main__":
    unittest.main()