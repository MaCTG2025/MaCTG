import unittest
from transform_object_image import transform_object_image
import numpy as np

class TestTransformObjectImage(unittest.TestCase):
    def test_empty_input(self):
        result = transform_object_image(None)
        self.assertTrue(np.array_equal(result, np.array([])))

    def test_single_pixel_image(self):
        single_pixel_image = np.array([[255]])
        result = transform_object_image(single_pixel_image)
        self.assertTrue(np.array_equal(result, np.array([[255]])))

    def test_square_image(self):
        square_image = np.array([
            [0, 0, 0],
            [0, 255, 0],
            [0, 0, 0]
        ])
        result = transform_object_image(square_image)
        self.assertEqual(result.shape, (1, 1))  # Check shape after downscaling and rotation

    def test_rectangular_image(self):
        rectangular_image = np.array([
            [0, 0, 0, 0],
            [0, 255, 255, 0],
            [0, 255, 255, 0],
            [0, 0, 0, 0]
        ])
        result = transform_object_image(rectangular_image)
        self.assertEqual(result.shape, (2, 2))  # Check shape after downscaling and rotation

if __name__ == '__main__':
    unittest.main()