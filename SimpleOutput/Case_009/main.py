from detect_and_draw_blobs import detect_and_draw_blobs

def blob_detection_module(image_path: str) -> None:
    """
    Detect blobs in the input image, draw bounding boxes around the detected blobs in red,
    and save the resulting image as 'blobs_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image where blobs need to be detected. The image should be in a format
        supported by OpenCV (e.g., JPEG, PNG).

    Returns:
    --------
    None
        The function does not return any value. It saves the resulting image with bounding boxes drawn
        around the detected blobs as 'blobs_image.png' in the current working directory.

    Example:
    --------
    blob_detection_module("./blobs.jpg")
    # This will detect blobs in 'blobs.jpg', draw red bounding boxes around them, and save the result as 'blobs_image.png'.
    """
    detect_and_draw_blobs(image_path)

if __name__ == '__main__':
    blob_detection_module("./blobs.jpg")