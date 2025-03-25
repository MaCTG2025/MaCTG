import unittest
from insert_seam import insert_seam
import numpy as np

class TestInsertSeam(unittest.TestCase):

    def test_insert_seam(self):
        # Create a sample image
        image = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [0, 255, 255], [255, 0, 255]]
        ], dtype=np.uint8)

        # Define a seam to insert
        seam = [1, 2]

        # Expected result after inserting the seam
        expected_result = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [0, 255, 255], [255, 0, 255], [255, 0, 255]]
        ], dtype=np.uint8)

        # Call the function
        result = insert_seam(image, seam)

        # Check if the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_result))

if __name__ == '__main__':
    unittest.main()