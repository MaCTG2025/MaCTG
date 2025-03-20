import unittest
from perform_pyramid_scaling import perform_pyramid_scaling
import cv2
import os

class TestPerformPyramidScaling(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.expected_upscaled_path = "./upscaled.png"
        self.expected_downscaled_path = "./downscaled.png"

    def test_perform_pyramid_scaling(self):
        # Ensure the test image exists
        self.assertTrue(os.path.exists(self.test_image_path))

        # Call the function
        result_paths = perform_pyramid_scaling(self.test_image_path)

        # Check if the returned paths match the expected paths
        self.assertEqual(result_paths[0], self.expected_upscaled_path)
        self.assertEqual(result_paths[1], self.expected_downscaled_path)

        # Check if the upscaled image exists
        self.assertTrue(os.path.exists(self.expected_upscaled_path))
        upscaled_image = cv2.imread(self.expected_upscaled_path)
        self.assertIsNotNone(upscaled_image)

        # Check if the downscaled image exists
        self.assertTrue(os.path.exists(self.expected_downscaled_path))
        downscaled_image = cv2.imread(self.expected_downscaled_path)
        self.assertIsNotNone(downscaled_image)

if __name__ == "__main__":
    unittest.main()