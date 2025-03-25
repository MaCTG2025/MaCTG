import unittest
from process_image_with_pyramid_scaling_and_orb import process_image_with_pyramid_scaling_and_orb
import cv2
import numpy as np
import os

class TestProcessImageWithPyramidScalingAndOrb(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.test_image_path, self.dummy_img)

    def tearDown(self):
        # Clean up generated files
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists("orb_upscaled.png"):
            os.remove("orb_upscaled.png")
        if os.path.exists("orb_downscaled.png"):
            os.remove("orb_downscaled.png")

    def test_process_image_with_pyramid_scaling_and_orb(self):
        # Call the function with default parameters
        process_image_with_pyramid_scaling_and_orb(self.test_image_path)

        # Check if the output images exist
        self.assertTrue(os.path.exists("orb_upscaled.png"))
        self.assertTrue(os.path.exists("orb_downscaled.png"))

if __name__ == "__main__":
    unittest.main()