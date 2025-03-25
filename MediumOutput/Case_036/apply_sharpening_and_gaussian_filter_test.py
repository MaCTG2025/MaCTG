import unittest
from apply_sharpening_and_gaussian_filter import apply_sharpening_and_gaussian_filter
import cv2
import numpy as np

class TestApplySharpeningAndGaussianFilter(unittest.TestCase):
    def test_apply_sharpening_and_gaussian_filter(self):
        # Define test parameters
        image_path = "test_image.png"
        sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        gaussian_kernel_size = (5, 5)
        sigmaX = 5
        output_path = "processed_image.png"

        # Call the function with test parameters
        apply_sharpening_and_gaussian_filter(
            image_path=image_path,
            sharpening_kernel=sharpening_kernel,
            gaussian_kernel_size=gaussian_kernel_size,
            sigmaX=sigmaX,
            output_path=output_path
        )

        # Load the processed image
        processed_image = cv2.imread(output_path)

        # Check if the image was loaded successfully
        self.assertIsNotNone(processed_image, "Processed image should not be None")

if __name__ == "__main__":
    unittest.main()