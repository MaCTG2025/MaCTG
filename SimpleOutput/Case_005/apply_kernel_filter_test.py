import unittest
from apply_kernel_filter import apply_kernel_filter
import cv2
import os
import numpy as np

class TestApplyKernelFilter(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.filtered_image_path = "./filtered_image.png"

    def test_apply_kernel_filter_exists(self):
        # Check if the test image exists
        self.assertTrue(os.path.exists(self.test_image_path))

    def test_apply_kernel_filter_output(self):
        # Apply the kernel filter
        apply_kernel_filter(self.test_image_path)

        # Check if the filtered image was created
        self.assertTrue(os.path.exists(self.filtered_image_path))

        # Load the original and filtered images
        original_image = cv2.imread(self.test_image_path)
        filtered_image = cv2.imread(self.filtered_image_path)

        # Calculate the mean squared error between the original and filtered images
        mse = np.mean((original_image.astype("float") - filtered_image.astype("float")) ** 2)

        # Assert that the MSE is less than a certain threshold (indicating blurring)
        self.assertLess(mse, 10000)

if __name__ == "__main__":
    unittest.main()