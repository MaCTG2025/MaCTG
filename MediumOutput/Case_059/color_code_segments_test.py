import unittest
from color_code_segments import color_code_segments
import numpy as np

class TestColorCodeSegments(unittest.TestCase):

    def test_valid_input(self):
        labels = np.array([0, 1, 2, 0, 1])
        centers = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
        image_shape = (2, 3, 3)
        
        expected_output = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
        ])
        
        output = color_code_segments(labels, centers, image_shape)
        self.assertTrue(np.array_equal(output, expected_output))

    def test_invalid_labels_type(self):
        labels = "not a numpy array"
        centers = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
        image_shape = (2, 3, 3)
        
        with self.assertRaises(ValueError):
            color_code_segments(labels, centers, image_shape)

    def test_invalid_centers_type(self):
        labels = np.array([0, 1, 2, 0, 1])
        centers = "not a numpy array"
        image_shape = (2, 3, 3)
        
        with self.assertRaises(ValueError):
            color_code_segments(labels, centers, image_shape)

    def test_invalid_image_shape_type(self):
        labels = np.array([0, 1, 2, 0, 1])
        centers = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
        image_shape = "not a tuple"
        
        with self.assertRaises(ValueError):
            color_code_segments(labels, centers, image_shape)

    def test_invalid_image_shape_length(self):
        labels = np.array([0, 1, 2, 0, 1])
        centers = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
        image_shape = (2, 3)
        
        with self.assertRaises(ValueError):
            color_code_segments(labels, centers, image_shape)

if __name__ == '__main__':
    unittest.main()