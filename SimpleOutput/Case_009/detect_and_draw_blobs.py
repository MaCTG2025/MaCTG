import cv2
import numpy as np

def detect_and_draw_blobs(image_path: str) -> None:
    """
    Detect blobs in the input image, draw bounding boxes around the detected blobs in red using drawKeypoints,
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

    Requirements:
    -------------
    1. The input image must exist at the specified path.
    2. The function uses OpenCV's SimpleBlobDetector to detect blobs.
    3. The bounding boxes are drawn in red using the `drawKeypoints` function.
    4. The resulting image is saved as 'blobs_image.png'.

    Example:
    --------
    detect_and_draw_blobs("./blobs.jpg")
    # This will detect blobs in 'blobs.jpg', draw red bounding boxes around them, and save the result as 'blobs_image.png'.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Set up the SimpleBlobDetector parameters
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 256
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 200
    
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    
    # Detect blobs.
    keypoints = detector.detect(image)
    
    # Draw detected blobs as red circles.
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Save the output image
    cv2.imwrite('blobs_image.png', im_with_keypoints)