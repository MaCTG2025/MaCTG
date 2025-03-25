import unittest
from process_and_fill_regions import process_and_fill_regions
import cv2
import numpy as np

class TestProcessAndFillRegions(unittest.TestCase):
    def test_process_and_fill_regions(self):
        # Define test parameters
        input_image_path = "test_image.png"
        output_image_path = "output_image.png"
        threshold1 = 100
        threshold2 = 200
        
        # Generate a sample image for testing
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(sample_image, (20, 20), (80, 80), (255, 255, 255), -1)
        cv2.imwrite(input_image_path, sample_image)
        
        # Call the function to be tested
        process_and_fill_regions(input_image_path, threshold1, threshold2, output_image_path)
        
        # Read the output image
        output_image = cv2.imread(output_image_path)
        
        # Check if the output image has the correct dimensions
        self.assertEqual(output_image.shape, (100, 100, 3))
        
        # Check if the filled region is green
        filled_region = output_image[20:80, 20:80]
        green_pixels = np.all(filled_region == [0, 255, 0], axis=-1)
        self.assertTrue(np.any(green_pixels))
        
        # Check if the edges remain visible
        edges = cv2.Canny(cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY), threshold1, threshold2)
        edge_pixels = np.any(edges > 0)
        self.assertTrue(edge_pixels)

if __name__ == "__main__":
    unittest.main()