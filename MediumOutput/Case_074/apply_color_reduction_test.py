import unittest
from apply_color_reduction import apply_color_reduction
import numpy as np
import os

class TestApplyColorReduction(unittest.TestCase):

    def test_valid_input(self):
        # Create sample regions
        region1 = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8)
        region2 = np.array([[[0, 255, 255], [255, 0, 255]], [[255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
        region3 = np.array([[[127, 127, 127], [191, 191, 191]], [[63, 63, 63], [223, 223, 223]]], dtype=np.uint8)
        region4 = np.array([[[255, 255, 255], [0, 0, 0]], [[127, 127, 127], [191, 191, 191]]], dtype=np.uint8)
        
        regions = [region1, region2, region3, region4]
        color_levels = [2, 3, 4, 5]
        output_path = "test_output.png"
        
        apply_color_reduction(regions, color_levels, output_path)
        
        # Check if the output file exists
        self.assertTrue(os.path.exists(output_path))
        
        # Clean up the output file
        os.remove(output_path)

    def test_invalid_regions_count(self):
        # Create sample regions
        region1 = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8)
        region2 = np.array([[[0, 255, 255], [255, 0, 255]], [[255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
        region3 = np.array([[[127, 127, 127], [191, 191, 191]], [[63, 63, 63], [223, 223, 223]]], dtype=np.uint8)
        
        regions = [region1, region2, region3]
        color_levels = [2, 3, 4]
        output_path = "test_output.png"
        
        with self.assertRaises(ValueError):
            apply_color_reduction(regions, color_levels, output_path)

    def test_invalid_color_levels_count(self):
        # Create sample regions
        region1 = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8)
        region2 = np.array([[[0, 255, 255], [255, 0, 255]], [[255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
        region3 = np.array([[[127, 127, 127], [191, 191, 191]], [[63, 63, 63], [223, 223, 223]]], dtype=np.uint8)
        region4 = np.array([[[255, 255, 255], [0, 0, 0]], [[127, 127, 127], [191, 191, 191]]], dtype=np.uint8)
        
        regions = [region1, region2, region3, region4]
        color_levels = [2, 3, 4]
        output_path = "test_output.png"
        
        with self.assertRaises(ValueError):
            apply_color_reduction(regions, color_levels, output_path)

if __name__ == '__main__':
    unittest.main()