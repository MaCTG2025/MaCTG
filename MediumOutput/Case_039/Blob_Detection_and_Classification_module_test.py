from Blob_Detection_and_Classification import blob_detection_and_classification_module

def test_blob_detection_and_classification_module(
    image_path: str = "./blobs.jpg",
    circularity_threshold: float = 0.7,
    inertia_threshold: float = 0.5,
    convexity_threshold: float = 0.9,
    output_image_path: str = "blobs_image.png"
) -> None:
    """
    Tests the blob_detection_and_classification_module function by detecting and classifying blobs in the provided image.

    Parameters:
    -----------
    image_path : str, optional (default="./blobs.jpg")
        The file path to the input image where blobs are to be detected.
    circularity_threshold : float, optional (default=0.7)
        The threshold for circularity to classify blobs.
    inertia_threshold : float, optional (default=0.5)
        The threshold for inertia to classify blobs.
    convexity_threshold : float, optional (default=0.9)
        The threshold for convexity to classify blobs.
    output_image_path : str, optional (default="blobs_image.png")
        The file path where the output image with highlighted blobs will be saved.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    try:
        blob_detection_and_classification_module(image_path, circularity_threshold, inertia_threshold, convexity_threshold, output_image_path)
        print("Test passed: The function executed successfully and saved the output image.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_blob_detection_and_classification_module()