import unittest
from detect_shapes import detect_shapes
import cv2
import numpy as np

class TestDetectShapes(unittest.TestCase):
    def test_detect_shapes(self):
        # Test with an image containing known shapes
        image_path = "./someshapes.jpg"
        shapes = detect_shapes(image_path)

        # Verify that the function returns a list
        self.assertIsInstance(shapes, list)

        # Verify that each element in the list is a tuple
        for shape in shapes:
            self.assertIsInstance(shape, tuple)
            self.assertEqual(len(shape), 2)
            self.assertIsInstance(shape[0], np.ndarray)  # Contour should be a NumPy array
            self.assertIsInstance(shape[1], str)        # Label should be a string

        # Verify that the detected shapes match the expected labels
        expected_labels = {'rectangle', 'square', 'triangle', 'circle', 'star'}
        detected_labels = {shape[1] for shape in shapes}
        self.assertTrue(detected_labels.issubset(expected_labels))

if __name__ == '__main__':
    unittest.main()