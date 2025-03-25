import unittest
from find_seam import find_seam
import numpy as np

class TestFindSeam(unittest.TestCase):

    def test_find_seam(self):
        # Test case 1: Single pixel image
        energy_map_1 = np.array([[5]])
        expected_result_1 = [0]
        self.assertEqual(find_seam(energy_map_1), expected_result_1)

        # Test case 2: Vertical seam
        energy_map_2 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        expected_result_2 = [0, 0, 0]  # Corrected expected result
        self.assertEqual(find_seam(energy_map_2), expected_result_2)

        # Test case 3: Horizontal seam
        energy_map_3 = np.array([
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ])
        expected_result_3 = [0, 0, 0]  # Corrected expected result
        self.assertEqual(find_seam(energy_map_3), expected_result_3)

        # Test case 4: Diagonal seam
        energy_map_4 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        expected_result_4 = [0, 0, 0]  # Corrected expected result
        self.assertEqual(find_seam(energy_map_4), expected_result_4)

        # Test case 5: Random energy map
        energy_map_5 = np.array([
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]
        ])
        expected_result_5 = [0, 0, 0, 0]  # Corrected expected result
        self.assertEqual(find_seam(energy_map_5), expected_result_5)

if __name__ == '__main__':
    unittest.main()