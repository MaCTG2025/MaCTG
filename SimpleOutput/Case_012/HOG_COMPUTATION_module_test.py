from HOG_COMPUTATION import hog_computation_module

def test_hog_computation_module() -> None:
    """
    Test the hog_computation_module function to ensure it computes and saves the HOG features correctly.
    """
    # Define test parameters
    image_path = "./test_image.png"  # Replace with a valid image path for testing
    cell_size = (8, 8)
    block_size = (2, 2)
    nbins = 9
    output_path = "hog.npy"

    # Call the module function
    hog_computation_module(image_path, cell_size, block_size, nbins, output_path)

    # Verify the output file exists
    import os
    assert os.path.exists(output_path), f"Output file {output_path} was not created."

    # Verify the output file is a valid .npy file
    import numpy as np
    try:
        hog_features = np.load(output_path)
        assert isinstance(hog_features, np.ndarray), f"Output file {output_path} does not contain a valid numpy array."
    except Exception as e:
        assert False, f"Failed to load output file {output_path}: {e}"

    print("Test passed: HOG features were computed and saved successfully.")

if __name__ == '__main__':
    test_hog_computation_module()