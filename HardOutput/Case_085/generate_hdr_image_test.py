import unittest
from generate_hdr_image import generate_hdr_image
import cv2
import numpy as np
import os

class TestGenerateHDRImage(unittest.TestCase):
    def test_generate_hdr_image(self):
        # Prepare test data
        image_paths = ["test_image1.exr", "test_image2.exr", "test_image3.exr"]
        exposure_times = [0.5, 2.0, 16.0]
        output_path = "output.hdr"

        # Mock the cv2.imread function to return dummy images
        def mock_imread(path, flags):
            if path == image_paths[0]:
                return np.random.randint(0, 256, size=(100, 100), dtype=np.uint16)
            elif path == image_paths[1]:
                return np.random.randint(0, 256, size=(100, 100), dtype=np.uint16)
            elif path == image_paths[2]:
                return np.random.randint(0, 256, size=(100, 100), dtype=np.uint16)
            else:
                raise ValueError("Invalid image path")

        cv2.imread = mock_imread

        # Call the function
        generate_hdr_image(image_paths, exposure_times, output_path)

        # Check if the output file exists
        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    unittest.main()