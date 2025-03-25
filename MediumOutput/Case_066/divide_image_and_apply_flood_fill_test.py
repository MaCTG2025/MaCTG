import unittest
from divide_image_and_apply_flood_fill import divide_image_and_apply_flood_fill
import cv2
import numpy as np

class TestDivideImageAndApplyFloodFill(unittest.TestCase):

    def test_divide_image_and_apply_flood_fill(self):
        # Load a sample image
        image_path = 'path_to_sample_image.jpg'
        segmented_image = divide_image_and_apply_flood_fill(image_path)

        # Check if the output image has the correct dimensions
        self.assertEqual(segmented_image.shape, (600, 800, 3))

        # Check if the regions are correctly highlighted
        top_left_region = segmented_image[0:300, 0:400]
        top_right_region = segmented_image[0:300, 400:]
        bottom_left_region = segmented_image[300:, 0:400]
        bottom_right_region = segmented_image[300:, 400:]

        # Check if the colors are correctly applied
        self.assertTrue(np.allclose(top_left_region[:, :, 2], 255))  # Red channel
        self.assertTrue(np.allclose(top_right_region[:, :, 1], 255))  # Green channel
        self.assertTrue(np.allclose(bottom_left_region[:, :, 0], 255))  # Blue channel
        self.assertTrue(np.allclose(bottom_right_region[:, :, 1], 255))  # Yellow (Green + Red)

if __name__ == '__main__':
    unittest.main()