import unittest
from segment_image_using_kmeans import segment_image_using_kmeans
import os

class TestSegmentImageUsingKMeans(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.jpg"
        self.output_image_path = "segmented_test_image.jpg"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_segment_image_with_valid_parameters(self):
        segment_image_using_kmeans(self.test_image_path, k=5, output_path=self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_segment_image_with_invalid_k_value(self):
        with self.assertRaises(ValueError):
            segment_image_using_kmeans(self.test_image_path, k=-1, output_path=self.output_image_path)

    def test_segment_image_with_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            segment_image_using_kmeans("nonexistent_image.jpg", k=5, output_path=self.output_image_path)

if __name__ == "__main__":
    unittest.main()