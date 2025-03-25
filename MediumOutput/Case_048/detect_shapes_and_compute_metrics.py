import cv2
import numpy as np

def detect_shapes_and_compute_metrics(image_path: str) -> None:
    """
    Detects shapes in the given image using OpenCV's connectedComponentsWithStats with connectivity=8.
    Computes the areas and perimeters of the detected shapes and saves the results into a .npy file.

    Args:
        image_path (str): The file path to the input image (e.g., "./shapes_r.png").

    Returns:
        None: The function does not return any value. It saves the computed areas and perimeters into a file
              named "areas_perimeters.npy".
    """
    # Load the image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply thresholding to convert the image to binary
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    # Find connected components with statistics
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)
    
    # Initialize lists to store areas and perimeters
    areas = []
    perimeters = []
    
    # Iterate over each shape (excluding the background label)
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        contours, _ = cv2.findContours((labels == i).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        perimeter = cv2.arcLength(contours[0], closed=True)
        
        areas.append(area)
        perimeters.append(perimeter)
    
    # Save the results to a .npy file
    np.save("areas_perimeters.npy", {"areas": areas, "perimeters": perimeters})