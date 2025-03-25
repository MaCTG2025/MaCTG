import unittest
from modify_image_hue import modify_image_hue
import cv2
import os

class TestModifyImageHue(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.modified_image_path = "./hue_modified_image.png"

    def test_modify_image_hue(self):
        # Load the original image
        original_image = cv2.imread(self.test_image_path)
        
        # Call the function to modify the image
        modify_image_hue(self.test_image_path)
        
        # Load the modified image
        modified_image = cv2.imread(self.modified_image_path)
        
        # Check if the modified image was created
        self.assertIsNotNone(modified_image)
        
        # Check if the dimensions of the original and modified images match
        self.assertEqual(original_image.shape, modified_image.shape)
        
        # Check if the Hue channel has been modified correctly
        hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
        hsv_modified = cv2.cvtColor(modified_image, cv2.COLOR_BGR2HSV)
        hue_original = hsv_original[:, :, 0]
        hue_modified = hsv_modified[:, :, 0]
        self.assertTrue(np.array_equal((hue_original + 50) % 180, hue_modified))

if __name__ == "__main__":
    unittest.main()