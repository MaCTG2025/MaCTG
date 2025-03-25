import unittest
from calculate_energy_map import calculate_energy_map
import numpy as np

class TestCalculateEnergyMap(unittest.TestCase):
    def test_calculate_energy_map(self):
        # Create a sample RGB image
        sample_image = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
            [[128, 128, 128], [64, 64, 64], [192, 192, 192]]
        ], dtype=np.uint8)

        # Expected energy map based on the sample image
        expected_energy_map = np.array([
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0.5]
        ])

        # Calculate the actual energy map
        actual_energy_map = calculate_energy_map(sample_image)

        # Check if the actual energy map is close to the expected energy map
        self.assertTrue(np.allclose(actual_energy_map, expected_energy_map, atol=0.1))

if __name__ == '__main__':
    unittest.main()