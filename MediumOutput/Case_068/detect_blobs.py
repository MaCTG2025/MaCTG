import cv2
import numpy as np

def detect_blobs(image_path: str) -> tuple[list[tuple[int, int, int]], np.ndarray]:
    """
    Detects blobs in the provided image.

    Args:
        image_path (str): The path to the input image file.

    Returns:
        blobs (list of tuples): A list of detected blobs, where each blob is represented as a tuple 
                                containing its centroid coordinates (x, y) and its area (area).
        image (np.ndarray): The image loaded as a NumPy array.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define the SimpleBlobDetector parameters
    params = cv2.SimpleBlobDetector_Params()
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 50
    
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    
    # Detect blobs
    keypoints = detector.detect(gray_image)
    
    # Extract centroids and areas
    blobs = [(int(keypoint.pt[0]), int(keypoint.pt[1]), int(keypoint.size**2)) for keypoint in keypoints]
    
    return blobs, image