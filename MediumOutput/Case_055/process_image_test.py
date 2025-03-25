import unittest
from process_image import process_image
import cv2
import numpy as np

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.png"
        self.output_image_path = "test_output.png"
        
        # Create a sample input image
        self.sample_image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(self.sample_image, (50, 50), (150, 150), (255, 255, 255), -1)
        cv2.imwrite(self.input_image_path, self.sample_image)

    def test_process_image(self):
        # Call the function to be tested
        process_image(self.input_image_path, self.output_image_path)
        
        # Read the processed image
        processed_image = cv2.imread(self.output_image_path, cv2.IMREAD_GRAYSCALE)
        
        # Check if the image was loaded successfully
        self.assertIsNotNone(processed_image)
        
        # Check the shape of the processed image
        self.assertEqual(processed_image.shape, (200, 200))
        
        # Check if the upper half is blurred
        upper_half_blurred = cv2.GaussianBlur(processed_image[:100, :], (21, 21), 11)
        self.assertTrue(np.array_equal(upper_half_blurred, processed_image[:100, :]))
        
        # Check if the lower half remains unchanged
        lower_half_unchanged = processed_image[100:, :]
        self.assertTrue(np.array_equal(lower_half_unchanged, cv2.cvtColor(self.sample_image[100:, :], cv2.COLOR_BGR2GRAY)))

if __name__ == '__main__':
    unittest.main()