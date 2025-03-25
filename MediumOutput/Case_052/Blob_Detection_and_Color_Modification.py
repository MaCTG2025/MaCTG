from detect_and_modify_blobs import detect_and_modify_blobs

def process_blobs(input_image_path: str, output_image_path: str) -> None:
    """
    Processes an input image to detect blobs, modifies the detected blob regions to red (R=255, G=0, B=0),
    and saves the modified image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image where blobs need to be detected. The image should be in a format
        supported by OpenCV (e.g., JPEG, PNG).
    
    output_image_path : str
        The file path where the modified image with red blobs will be saved. The output format will be
        determined by the file extension (e.g., ".png").

    Returns:
    --------
    None
        The function does not return any value. It saves the modified image directly to disk.
    """
    detect_and_modify_blobs(input_image_path, output_image_path)