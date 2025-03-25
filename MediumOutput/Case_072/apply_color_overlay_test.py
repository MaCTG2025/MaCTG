import unittest
from apply_color_overlay import apply_color_overlay
import cv2
import numpy as np

class TestApplyColorOverlay(unittest.TestCase):
    def test_apply_color_overlay(self):
        # Load test data
        image_path = 'test_image.jpg'
        binary_mask = np.zeros((100, 100), dtype=np.uint8)
        binary_mask[30:70, 30:70] = 255
        
        # Call the function
        result_image = apply_color_overlay(image_path, binary_mask)
        
        # Check if the result image has the correct shape
        self.assertEqual(result_image.shape, (100, 100, 3))
        
        # Check if the masked region is black
        self.assertTrue(np.allclose(result_image[30:70, 30:70], [0, 0, 0]))
        
        # Check if the non-masked region is unchanged
        self.assertTrue(np.allclose(result_image[:30, :30], cv2.imread(image_path)[:30, :30]))
        self.assertTrue(np.allclose(result_image[70:, 70:], cv2.imread(image_path)[70:, 70:]))

        # Test with different mask weights
        result_image = apply_color_overlay(image_path, binary_mask, mask_weight=0.5, image_weight=0.5)
        self.assertEqual(result_image.shape, (100, 100, 3))

        # Test with invalid mask shape
        invalid_mask = np.zeros((50, 50), dtype=np.uint8)
        with self.assertRaises(ValueError):
            apply_color_overlay(image_path, invalid_mask)

if __name__ == '__main__':
    unittest.main()