import numpy as np
from Feature_Extraction_Module import feature_extraction_module

def test_Feature_Extraction_Module(image_path: str) -> None:
    """
    Tests the basic functionality of the Feature_Extraction_Module.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").

    Returns:
        None: The function verifies that the HOG and LBP features are saved correctly.
    """
    # Call the module function
    feature_extraction_module(image_path)

    # Verify that the output files exist
    try:
        hog_features = np.load("hog_features.npy")
        lbp_features = np.load("lbp_features.npy")
        print("Test passed: HOG and LBP features were saved successfully.")
        print(f"HOG features shape: {hog_features.shape}")
        print(f"LBP features shape: {lbp_features.shape}")
    except FileNotFoundError:
        print("Test failed: Output files (hog_features.npy or lbp_features.npy) were not found.")

if __name__ == '__main__':
    test_Feature_Extraction_Module("./test_image.png")