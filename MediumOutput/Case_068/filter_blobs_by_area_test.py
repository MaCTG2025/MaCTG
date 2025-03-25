import unittest
from filter_blobs_by_area import filter_blobs_by_area
import cv2
import numpy as np

class TestFilterBlobsByArea(unittest.TestCase):
    def test_filter_blobs_by_area(self):
        # Test case 1: Empty list of blobs
        blobs = []
        min_area = 10
        max_area = 50
        expected_result = []
        self.assertEqual(filter_blobs_by_area(blobs, min_area, max_area), expected_result)

        # Test case 2: Blobs with areas outside the specified range
        blobs = [(10, 10, 5), (20, 20, 60)]
        min_area = 10
        max_area = 50
        expected_result = []
        self.assertEqual(filter_blobs_by_area(blobs, min_area, max_area), expected_result)

        # Test case 3: Blobs with areas within the specified range
        blobs = [(10, 10, 25), (20, 20, 40)]
        min_area = 10
        max_area = 50
        expected_result = [(10, 10, 25), (20, 20, 40)]
        self.assertEqual(filter_blobs_by_area(blobs, min_area, max_area), expected_result)

        # Test case 4: Blobs with some areas within and some outside the specified range
        blobs = [(10, 10, 25), (20, 20, 60), (30, 30, 35)]
        min_area = 10
        max_area = 50
        expected_result = [(10, 10, 25), (30, 30, 35)]
        self.assertEqual(filter_blobs_by_area(blobs, min_area, max_area), expected_result)

if __name__ == '__main__':
    unittest.main()