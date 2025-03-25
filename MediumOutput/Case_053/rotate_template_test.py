import unittest
from rotate_template import rotate_template
import numpy as np

class TestRotateTemplate(unittest.TestCase):
    def test_rotate_0_degrees(self):
        # Create a sample image
        image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
        
        # Rotate the image by 0 degrees
        rotated_image = rotate_template(image, 0)
        
        # Check if the image remains unchanged
        self.assertTrue(np.array_equal(image, rotated_image))
    
    def test_rotate_45_degrees(self):
        # Create a sample image
        image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
        
        # Rotate the image by 45 degrees
        rotated_image = rotate_template(image, 45)
        
        # Check if the image has been rotated correctly
        expected_image = np.array([[0, 2], [1, 4]], dtype=np.uint8)
        self.assertTrue(np.array_equal(rotated_image, expected_image))
    
    def test_rotate_90_degrees(self):
        # Create a sample image
        image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
        
        # Rotate the image by 90 degrees
        rotated_image = rotate_template(image, 90)
        
        # Check if the image has been rotated correctly
        expected_image = np.array([[3, 1], [4, 2]], dtype=np.uint8)
        self.assertTrue(np.array_equal(rotated_image, expected_image))
    
    def test_rotate_135_degrees(self):
        # Create a sample image
        image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
        
        # Rotate the image by 135 degrees
        rotated_image = rotate_template(image, 135)
        
        # Check if the image has been rotated correctly
        expected_image = np.array([[2, 0], [4, 1]], dtype=np.uint8)
        self.assertTrue(np.array_equal(rotated_image, expected_image))

if __name__ == '__main__':
    unittest.main()