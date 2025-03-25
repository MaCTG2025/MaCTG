from detect_and_analyze_blobs import detect_and_analyze_blobs

def blob_detection_and_analysis_module(image_path: str, output_path: str) -> None:
    """
    Detects blobs in the given image, computes the center, area, and perimeter for each blob,
    and saves the results into a .npy file.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./blobs.jpg"). The image should be in a format
        supported by OpenCV (e.g., JPEG, PNG).
    output_path : str
        The file path where the results will be saved (e.g., "blobs.npy"). The output will be
        saved as a NumPy array in .npy format.

    Returns:
    --------
    None
        The function does not return any value directly. Instead, it saves the results to the
        specified output file.

    Example:
    --------
    blob_detection_and_analysis_module("./blobs.jpg", "blobs.npy")
    """
    detect_and_analyze_blobs(image_path, output_path)