from detect_and_classify_blobs import detect_and_classify_blobs

def blob_detection_and_classification_module(
    image_path: str,
    circularity_threshold: float = 0.7,
    inertia_threshold: float = 0.5,
    convexity_threshold: float = 0.9,
    output_image_path: str = "blobs_image.png"
) -> None:
    """
    Detects and classifies blobs in the provided image using SimpleBlobDetector, and saves the image with highlighted blobs.

    Parameters:
    -----------
    image_path : str
        The file path to the input image where blobs are to be detected.
    circularity_threshold : float, optional (default=0.7)
        The threshold for circularity to classify blobs. Blobs with circularity below this threshold will be filtered out.
    inertia_threshold : float, optional (default=0.5)
        The threshold for inertia to classify blobs. Blobs with inertia below this threshold will be filtered out.
    convexity_threshold : float, optional (default=0.9)
        The threshold for convexity to classify blobs. Blobs with convexity below this threshold will be filtered out.
    output_image_path : str, optional (default="blobs_image.png")
        The file path where the output image with highlighted blobs will be saved.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image to the specified output path.
    """
    detect_and_classify_blobs(image_path, circularity_threshold, inertia_threshold, convexity_threshold, output_image_path)