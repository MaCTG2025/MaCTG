import unittest
from process_and_mask_image import process_and_mask_image
import cv2
import numpy as np

class TestProcessAndMaskImage(unittest.TestCase):
    def test_process_and_mask_image(self):
        # Load a sample image
        sample_image_path = "sample_image.png"
        sample_image = cv2.imread(sample_image_path)

        # Process the sample image using the function
        process_and_mask_image(sample_image_path)

        # Load the masked image
        masked_image = cv2.imread("masked_image.png")

        # Check if the masked image has the same dimensions as the sample image
        self.assertEqual(masked_image.shape, sample_image.shape)

        # Check if the masked image has a circular region with zero values in the Hue channel
        height, width = masked_image.shape[:2]
        center = (width // 2, height // 2)
        mask = np.zeros((height, width), dtype=np.uint8)
        cv2.circle(mask, center, 100, (255), -1)
        masked_hue_channel = cv2.cvtColor(masked_image, cv2.COLOR_RGB2HSV)[:, :, 0]
        non_zero_pixels = np.sum(masked_hue_channel[mask == 255])
        self.assertEqual(non_zero_pixels, 0)

if __name__ == "__main__":
    unittest.main()