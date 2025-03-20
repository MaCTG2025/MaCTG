import unittest
from detect_vertical_symmetry import detect_vertical_symmetry
import cv2
import numpy as np

class TestDetectVerticalSymmetry(unittest.TestCase):
    def test_symmetric_image(self):
        # Create a symmetric image
        width, height = 200, 200
        symmetric_image = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.rectangle(symmetric_image, (0, 0), (width // 2, height), (255, 255, 255), -1)
        cv2.rectangle(symmetric_image, (width // 2, 0), (width, height), (255, 255, 255), -1)
        
        # Save the symmetric image temporarily
        temp_image_path = 'temp_symmetric_image.png'
        cv2.imwrite(temp_image_path, symmetric_image)
        
        # Call the function with the temporary image
        axis_x, result_image = detect_vertical_symmetry(temp_image_path)
        
        # Check if the symmetry axis is correctly detected
        self.assertEqual(axis_x, width // 2)
        
        # Check if the result image matches the original symmetric image
        self.assertTrue(np.array_equal(result_image, symmetric_image))

    def test_asymmetric_image(self):
        # Create an asymmetric image
        width, height = 200, 200
        asymmetric_image = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.rectangle(asymmetric_image, (0, 0), (width // 2, height), (255, 255, 255), -1)
        cv2.rectangle(asymmetric_image, (width // 2 + 10, 0), (width, height), (255, 255, 255), -1)
        
        # Save the asymmetric image temporarily
        temp_image_path = 'temp_asymmetric_image.png'
        cv2.imwrite(temp_image_path, asymmetric_image)
        
        # Call the function with the temporary image
        axis_x, result_image = detect_vertical_symmetry(temp_image_path)
        
        # Check if the symmetry axis is correctly detected (should be None)
        self.assertIsNone(axis_x)
        
        # Check if the result image matches the original asymmetric image
        self.assertTrue(np.array_equal(result_image, asymmetric_image))

if __name__ == '__main__':
    unittest.main()