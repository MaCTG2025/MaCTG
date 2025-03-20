import cv2
import numpy as np
from skimage.measure import label, regionprops

def extract_largest_connected_component(image_path: str) -> None:
    """
    Processes the input image to identify and extract the largest connected component (excluding the background),
    switches all other pixels to black, and saves the resulting image as 'largest_connected_component.png'.

    The function performs the following steps:
    1. Reads the input image from the provided file path.
    2. Converts the image to grayscale if it is not already in grayscale.
    3. Thresholds the image to create a binary mask (assuming the background is black or white).
    4. Uses connected component analysis to identify all connected components in the image.
    5. Identifies the largest connected component (excluding the background).
    6. Creates a new image where all pixels not belonging to the largest connected component are set to black.
    7. Saves the resulting image as 'largest_connected_component.png' in the current working directory.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image as 'largest_connected_component.png'.

    Dependencies:
    ------------
    - OpenCV (cv2): For reading, processing, and saving images.
    - NumPy (numpy): For array manipulation.
    - scikit-image (skimage.measure): For connected component analysis and region properties.

    Example:
    --------
    extract_largest_connected_component("./shapes_r.png")
    # This will save the largest connected component as 'largest_connected_component.png'.
    """
    # Read the input image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale if it is not already in grayscale
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    
    # Threshold the image to create a binary mask
    _, binary_mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Perform connected component analysis
    labeled_array, num_features = label(binary_mask, return_num=True)
    
    # Get region properties of each connected component
    regions = regionprops(labeled_array)
    
    # Find the largest connected component (excluding the background)
    max_area = 0
    largest_region_label = 0
    for region in regions:
        if region.area > max_area:
            max_area = region.area
            largest_region_label = region.label
    
    # Create a new image where all pixels not belonging to the largest connected component are set to black
    result_image = np.zeros_like(binary_mask)
    result_image[labeled_array == largest_region_label] = 255
    
    # Save the resulting image
    cv2.imwrite('largest_connected_component.png', result_image)