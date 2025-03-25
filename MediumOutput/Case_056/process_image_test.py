import unittest
from process_image import process_image
import cv2
import numpy as np
import os

class TestProcessImage(unittest.TestCase):
    def test_process_image(self):
        # Create a sample image
        sample_image = np.array([
            [[255, 0, 0], [0, 255, 0]],
            [[0, 0, 255], [255, 255, 255]]
        ], dtype=np.uint8)
        
        # Define temporary paths for input and output images
        input_path = 'temp_input.png'
        output_path = 'temp_output.png'
        
        # Save the sample image to the input path
        cv2.imwrite(input_path, sample_image)
        
        # Call the process_image function
        process_image(input_path, output_path)
        
        # Read the processed image from the output path
        processed_image = cv2.imread(output_path)
        
        # Check if the processed image is not None
        self.assertIsNotNone(processed_image)
        
        # Clean up temporary files
        os.remove(input_path)
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()