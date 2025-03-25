import unittest
from process_image_with_pyramid_and_corners import process_image_with_pyramid_and_corners
import os

class TestProcessImageWithPyramidAndCorners(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.png"
        self.scales = [1.0, 0.5, 0.25]

    def test_process_image_with_pyramid_and_corners(self):
        process_image_with_pyramid_and_corners(self.image_path, self.scales)
        for scale in self.scales:
            output_filename = f"{self.image_path.split('.')[0]}_corners_x{scale:.1f}.png"
            self.assertTrue(os.path.exists(output_filename))

if __name__ == "__main__":
    unittest.main()