import unittest
from embed_watermark import embed_watermark
import cv2
import os

class TestEmbedWatermark(unittest.TestCase):

    def setUp(self):
        self.input_image_path = "test_image.png"
        self.output_image_path = "watermarked_image.png"

    def test_embed_watermark_with_color_image(self):
        embed_watermark(self.input_image_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_embed_watermark_with_grayscale_image(self):
        gray_image_path = "gray_test_image.png"
        cv2.imwrite(gray_image_path, cv2.cvtColor(cv2.imread(self.input_image_path), cv2.COLOR_BGR2GRAY))
        embed_watermark(gray_image_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

if __name__ == '__main__':
    unittest.main()