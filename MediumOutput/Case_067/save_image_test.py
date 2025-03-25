import unittest
from save_image import save_image
import cv2
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)

        # Define a temporary file path
        temp_file_path = "temp_image.png"

        # Save the image
        save_image(sample_image, temp_file_path)

        # Check if the file exists
        self.assertTrue(os.path.exists(temp_file_path))

        # Read the saved image back
        loaded_image = cv2.imread(temp_file_path)

        # Check if the loaded image matches the sample image
        self.assertTrue(np.array_equal(sample_image, loaded_image))

if __name__ == "__main__":
    unittest.main()