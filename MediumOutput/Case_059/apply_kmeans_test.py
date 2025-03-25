import unittest
from apply_kmeans import apply_kmeans
import numpy as np

class TestApplyKMeans(unittest.TestCase):

    def test_valid_input(self):
        # Create a sample image with 3x3 pixels and 3 channels
        image = np.array([[[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]]])
        k = 2
        labels, centers = apply_kmeans(image, k)
        self.assertEqual(labels.shape, (9,))
        self.assertEqual(centers.shape, (2, 3))

    def test_invalid_image_type(self):
        # Provide an invalid image type
        image = "not_an_array"
        k = 2
        with self.assertRaises(ValueError):
            apply_kmeans(image, k)

    def test_invalid_k_value(self):
        # Provide an invalid k value
        image = np.array([[[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]]])
        k = 0
        with self.assertRaises(ValueError):
            apply_kmeans(image, k)

    def test_single_cluster(self):
        # Test with a single cluster
        image = np.array([[[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]],
                          [[0, 0, 0], [128, 128, 128], [255, 255, 255]]])
        k = 1
        labels, centers = apply_kmeans(image, k)
        self.assertEqual(labels.shape, (9,))
        self.assertEqual(centers.shape, (1, 3))
        self.assertTrue(np.all(labels == 0))

if __name__ == '__main__':
    unittest.main()