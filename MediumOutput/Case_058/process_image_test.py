import unittest
from process_image import process_image
import cv2
import numpy as np

class TestProcessImage(unittest.TestCase):

    def test_process_image(self):
        # Define test parameters
        input_path = "./test_image.png"
        output_path = "./processed_test_image.png"
        
        # Call the function
        process_image(input_path, output_path=output_path)
        
        # Load the processed image
        processed_image = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        
        # Check if the image is loaded successfully
        self.assertIsNotNone(processed_image)
        
        # Check if the image has the same dimensions as the input image
        input_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        self.assertEqual(processed_image.shape, input_image.shape)

        # Check if the processed image is not identical to the input image
        self.assertFalse(np.array_equal(processed_image, input_image))

if __name__ == "__main__":
    unittest.main()