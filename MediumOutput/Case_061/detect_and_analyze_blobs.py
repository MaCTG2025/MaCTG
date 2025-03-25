import cv2
import numpy as np
from skimage.measure import regionprops

def detect_and_analyze_blobs(image_path: str, output_path: str) -> None:
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

    Requirements:
    -------------
    1. The input image must exist at the specified path and be in a format supported by OpenCV.
    2. The function uses OpenCV for blob detection and skimage.measure.regionprops for computing
       blob properties (center, area, and perimeter).
    3. The output file will contain a NumPy array with the following data for each detected blob:
       - Center coordinates (x, y) as a tuple of floats.
       - Area (in pixels) as a float.
       - Perimeter (in pixels) as a float.

    Example:
    --------
    detect_and_analyze_blobs("./blobs.jpg", "blobs.npy")
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve blob detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Perform thresholding to create a binary image
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Prepare a list to store blob properties
    blob_properties = []
    
    # Iterate over each contour to compute properties
    for contour in contours:
        # Compute the region properties
        props = regionprops(contour)
        
        # Extract center, area, and perimeter
        center = props[0].centroid
        area = props[0].area
        perimeter = props[0].perimeter
        
        # Append the properties to the list
        blob_properties.append([center, area, perimeter])
    
    # Convert the list to a NumPy array
    blob_array = np.array(blob_properties)
    
    # Save the NumPy array to the specified output file
    np.save(output_path, blob_array)