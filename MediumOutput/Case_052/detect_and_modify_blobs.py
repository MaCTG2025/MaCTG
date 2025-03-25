import cv2
import numpy as np

def detect_and_modify_blobs(input_image_path: str, output_image_path: str) -> None:
    """
    Detects all blobs in the input image, changes the color of the detected blob regions to red (R=255, G=0, B=0),
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

    Requirements:
    -------------
    1. The function should use OpenCV's blob detection methods (e.g., SimpleBlobDetector) to identify blobs
       in the input image.
    2. After detecting the blobs, the function should modify the pixel values in the blob regions to red
       (R=255, G=0, B=0).
    3. The modified image should be saved to the specified output path in PNG format.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing and blob detection.
    - NumPy (numpy) for array manipulation.

    Example:
    --------
    detect_and_modify_blobs("./blobs.jpg", "blobs_red.png")
    """
    # Load the image
    image = cv2.imread(input_image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Set up the SimpleBlobDetector parameters
    params = cv2.SimpleBlobDetector_Params()
    
    # Filter by Color
    params.filterByColor = True
    params.blobColor = 255
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 50
    
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    
    # Detect blobs.
    keypoints = detector.detect(gray)
    
    # Draw detected blobs as red circles.
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Save the image with the red blobs
    cv2.imwrite(output_image_path, im_with_keypoints)