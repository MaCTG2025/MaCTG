import unittest
from detect_and_analyze_blobs import detect_and_analyze_blobs
import cv2
import numpy as np

class TestDetectAndAnalyzeBlobs(unittest.TestCase):
    def test_detect_and_analyze_blobs(self):
        # Create a sample image with known blobs
        image = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(image, (50, 50), 20, 255, -1)  # Blob 1
        cv2.circle(image, (70, 70), 15, 255, -1)  # Blob 2
        
        # Define the expected output
        expected_output = np.array([[(50.0, 50.0), 400.0, 125.66370614359172],
                                    [(70.0, 70.0), 225.0, 94.24777960769379]])
        
        # Define temporary paths for input and output
        temp_input_path = 'temp_input.png'
        temp_output_path = 'temp_output.npy'
        
        # Save the sample image to the temporary input path
        cv2.imwrite(temp_input_path, image)
        
        # Call the function under test
        detect_and_analyze_blobs(temp_input_path, temp_output_path)
        
        # Load the generated output from the temporary output path
        actual_output = np.load(temp_output_path)
        
        # Compare the actual output with the expected output
        np.testing.assert_almost_equal(actual_output, expected_output, decimal=5)

if __name__ == '__main__':
    unittest.main()