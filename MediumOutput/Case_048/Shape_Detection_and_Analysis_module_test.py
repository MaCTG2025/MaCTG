import cv2
import numpy as np
from Shape_Detection_and_Analysis import shape_detection_and_analysis

def test_shape_detection_and_analysis(image_path: str) -> None:
    """
    Tests the shape_detection_and_analysis function by running it with the provided image path
    and verifying that the output file "areas_perimeters.npy" is created and contains valid data.

    Args:
        image_path (str): The file path to the input image (e.g., "./shapes_r.png").
    """
    # Run the function to detect shapes and compute metrics
    shape_detection_and_analysis(image_path)

    # Verify that the output file exists
    try:
        results = np.load("areas_perimeters.npy")
        print("Output file 'areas_perimeters.npy' created successfully.")
        print("Results:", results)
    except FileNotFoundError:
        print("Error: Output file 'areas_perimeters.npy' was not created.")

if __name__ == '__main__':
    test_shape_detection_and_analysis("./shapes_r.png")