import unittest
from detect_and_modify_blobs import detect_and_modify_blobs
import cv2
import numpy as np

class TestDetectAndModifyBlobs(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.output_image_path = "test_output.png"
        
        # Create a sample input image with a blob
        self.sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.circle(self.sample_image, (50, 50), 20, (255, 255, 255), -1)
        cv2.imwrite(self.input_image_path, self.sample_image)

    def test_detect_and_modify_blobs(self):
        detect_and_modify_blobs(self.input_image_path, self.output_image_path)
        
        # Load the output image
        output_image = cv2.imread(self.output_image_path)
        
        # Check if the output image has the correct dimensions
        self.assertEqual(output_image.shape, (100, 100, 3))
        
        # Check if the blob region is red
        blob_region = output_image[40:60, 40:60]
        red_pixels = np.sum(blob_region[:, :, 2] == 255)
        green_pixels = np.sum(blob_region[:, :, 1] == 0)
        blue_pixels = np.sum(blob_region[:, :, 0] == 0)
        self.assertGreater(red_pixels, 0)
        self.assertEqual(green_pixels, 0)
        self.assertEqual(blue_pixels, 0)

if __name__ == '__main__':
    unittest.main()