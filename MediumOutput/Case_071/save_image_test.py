import unittest
from save_image import save_image
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image_success(self):
        result_image = np.zeros((100, 100, 3), dtype=np.uint8)
        output_path = "test_output.jpg"
        save_image(result_image, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)  # Clean up after the test

    def test_save_image_failure(self):
        result_image = np.zeros((100, 100, 3), dtype=np.uint8)
        with self.assertRaises(IOError):
            save_image(result_image, "/nonexistent/path/test_output.jpg")

if __name__ == "__main__":
    unittest.main()