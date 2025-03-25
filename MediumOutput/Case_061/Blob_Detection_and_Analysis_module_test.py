from Blob_Detection_and_Analysis import blob_detection_and_analysis_module

def test_blob_detection_and_analysis_module(image_path: str, output_path: str) -> None:
    """
    Tests the blob_detection_and_analysis_module function to ensure it works as expected.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./blobs.jpg").
    output_path : str
        The file path where the results will be saved (e.g., "blobs.npy").

    Returns:
    --------
    None
        The function does not return any value but prints a success message if the test passes.
    """
    try:
        blob_detection_and_analysis_module(image_path, output_path)
        print("Test passed: blob_detection_and_analysis_module executed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_blob_detection_and_analysis_module("./blobs.jpg", "blobs.npy")