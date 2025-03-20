import unittest
from rescale_and_save_image import rescale_and_save_image
import os
import cv2

class TestRescaleAndSaveImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.rescaled_images = ["linear_interpolation.png", "cubic_interpolation.png", "area_interpolation.png"]

    def test_rescale_and_save_image_exists(self):
        rescale_and_save_image(self.test_image_path)
        for img in self.rescaled_images:
            self.assertTrue(os.path.exists(img))

    def test_rescale_and_save_image_dimensions(self):
        rescale_and_save_image(self.test_image_path)
        original_image = cv2.imread(self.test_image_path)
        original_height, original_width = original_image.shape[:2]
        for img in self.rescaled_images:
            rescaled_image = cv2.imread(img)
            rescaled_height, rescaled_width = rescaled_image.shape[:2]
            self.assertEqual(rescaled_height, original_height * 2)
            self.assertEqual(rescaled_width, original_width * 2)

if __name__ == "__main__":
    unittest.main()