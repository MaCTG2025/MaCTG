import unittest
from compare_gradients import compare_gradients
import numpy as np

class TestCompareGradients(unittest.TestCase):

    def test_valid_input(self):
        grad1 = np.array([[1, 2], [3, 4]])
        grad2 = np.array([[5, 6], [7, 8]])
        expected_output = np.array([[4, 4], [4, 4]])
        self.assertTrue(np.array_equal(compare_gradients(grad1, grad2), expected_output))

    def test_different_shapes(self):
        grad1 = np.array([[1, 2], [3, 4]])
        grad2 = np.array([[5, 6]])
        with self.assertRaises(ValueError):
            compare_gradients(grad1, grad2)

    def test_non_array_input(self):
        grad1 = [[1, 2], [3, 4]]
        grad2 = np.array([[5, 6], [7, 8]])
        with self.assertRaises(ValueError):
            compare_gradients(grad1, grad2)

if __name__ == '__main__':
    unittest.main()