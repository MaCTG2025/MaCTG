import cv2
import numpy as np

def process_image(
    image_path: str,
    d: int = 9,
    sigmaColor: float = 75.0,
    sigmaSpace: float = 75.0,
    ksize: int = 5,
    nms_threshold: int = 100,
    output_path: str = "test_image_edges.png"
) -> None:
    """
    Applies bilateral filtering to reduce noise while preserving edges, computes gradient magnitudes using Sobel operators,
    applies non-maximum suppression to enhance the most prominent edges, and saves the processed image.

    Steps:
    1. Load the image from the specified `image_path`.
    2. Apply bilateral filtering to the image using the provided parameters:
       - `d`: Diameter of each pixel neighborhood used during filtering.
       - `sigmaColor`: Filter sigma in the color space.
       - `sigmaSpace`: Filter sigma in the coordinate space.
    3. Compute gradient magnitudes using Sobel operators with the specified kernel size (`ksize`).
    4. Apply non-maximum suppression (NMS) to the gradient magnitudes using the provided `nms_threshold`.
    5. Save the resulting image to the specified `output_path`.

    Parameters:
    -----------
    image_path : str
        Path to the input image file.
    d : int, optional
        Diameter of each pixel neighborhood used in bilateral filtering (default=9).
    sigmaColor : float, optional
        Filter sigma in the color space for bilateral filtering (default=75.0).
    sigmaSpace : float, optional
        Filter sigma in the coordinate space for bilateral filtering (default=75.0).
    ksize : int, optional
        Kernel size for Sobel operators (default=5).
    nms_threshold : int, optional
        Threshold value for non-maximum suppression (default=100).
    output_path : str, optional
        Path to save the processed image (default="test_image_edges.png").

    Returns:
    --------
    None
        The function saves the processed image to the specified `output_path`.

    Example:
    --------
    process_image("./test_image.png", d=9, sigmaColor=75, sigmaSpace=75, ksize=5, nms_threshold=100, output_path="test_image_edges.png")
    """
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply bilateral filtering
    filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    
    # Compute gradient magnitudes using Sobel operators
    sobelx = cv2.Sobel(filtered_image, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(filtered_image, cv2.CV_64F, 0, 1, ksize=ksize)
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    
    # Apply non-maximum suppression
    suppressed_image = np.zeros_like(gradient_magnitude)
    rows, cols = gradient_magnitude.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            angle = np.arctan2(sobely[i,j], sobelx[i,j]) * 180 / np.pi
            angle = round(angle / 45) * 45
            
            if angle == 0 or angle == 180:
                neighbors = [gradient_magnitude[i,j-1], gradient_magnitude[i,j+1]]
            elif angle == 45:
                neighbors = [gradient_magnitude[i-1,j+1], gradient_magnitude[i+1,j-1]]
            elif angle == 90:
                neighbors = [gradient_magnitude[i-1,j], gradient_magnitude[i+1,j]]
            else:  # angle == 135
                neighbors = [gradient_magnitude[i-1,j-1], gradient_magnitude[i+1,j+1]]
            
            if gradient_magnitude[i,j] >= max(neighbors):
                suppressed_image[i,j] = gradient_magnitude[i,j]
    
    # Save the processed image
    cv2.imwrite(output_path, suppressed_image)