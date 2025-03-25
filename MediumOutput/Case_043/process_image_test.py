import unittest
from process_image import process_image
import cv2
import numpy as np

class TestProcessImage(unittest.TestCase):
    def test_process_image(self):
        # Define test parameters
        input_image_path = "test_image.png"
        cascade_path = "haarcascade_frontalface_default.xml"
        output_image_path = "processed_test_image.png"
        
        # Generate a sample image with a face for testing
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(image, (50, 50), (150, 150), (255, 255, 255), -1)
        cv2.imwrite(input_image_path, image)
        
        # Call the process_image function
        process_image(input_image_path, cascade_path, output_path=output_image_path)
        
        # Load the processed image
        processed_image = cv2.imread(output_image_path)
        
        # Check if the image has been processed correctly
        self.assertTrue(np.any(processed_image != image))

if __name__ == "__main__":
    unittest.main()