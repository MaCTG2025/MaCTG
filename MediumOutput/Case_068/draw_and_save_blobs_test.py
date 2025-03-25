import unittest
from draw_and_save_blobs import draw_and_save_blobs
import numpy as np
import os
import cv2

class TestDrawAndSaveBlobs(unittest.TestCase):
    def setUp(self):
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.filtered_blobs = [(50, 50, 10)]
        self.output_path = "test_output.png"

    def test_draw_and_save_blobs(self):
        draw_and_save_blobs(self.image, self.filtered_blobs, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        loaded_image = cv2.imread(self.output_path)
        self.assertEqual(loaded_image.shape, (100, 100, 3))
        self.assertEqual(loaded_image[50, 50].tolist(), [0, 255, 0])

if __name__ == "__main__":
    unittest.main()