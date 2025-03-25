import cv2
import numpy as np

def process_image(image_path: str, output_path: str) -> None:
    """
    Combines all the above functions into a single high-level function for convenience.
    The function performs the following steps:
        1. Converts the input image to grayscale.
        2. Divides the grayscale image into four quadrants.
        3. Processes each quadrant with specific operations.
        4. Combines the processed quadrants into a single image.
        5. Saves the processed image to the specified output path.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the processed image.

    Returns:
        None: The processed image is saved to disk.

    Requirements:
        - The input image must be a valid image file.
        - The function calls `convert_to_grayscale`, `divide_into_quadrants`, `process_quadrants`, `combine_quadrants`, and `save_image` in sequence.
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = convert_to_grayscale(image)
    
    # Divide the grayscale image into four quadrants
    quadrants = divide_into_quadrants(gray_image)
    
    # Process each quadrant
    processed_quadrants = process_quadrants(quadrants)
    
    # Combine the processed quadrants into a single image
    combined_image = combine_quadrants(processed_quadrants)
    
    # Save the processed image to the specified output path
    save_image(combined_image, output_path)

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def divide_into_quadrants(image):
    """Divides an image into four quadrants."""
    height, width = image.shape[:2]
    top_left = image[0:height//2, 0:width//2]
    top_right = image[0:height//2, width//2:]
    bottom_left = image[height//2:, 0:width//2]
    bottom_right = image[height//2:, width//2:]
    return [top_left, top_right, bottom_left, bottom_right]

def process_quadrants(quadrants):
    """Processes each quadrant with specific operations."""
    processed_quadrants = []
    for quadrant in quadrants:
        # Example processing: invert the colors
        inverted_quadrant = cv2.bitwise_not(quadrant)
        processed_quadrants.append(inverted_quadrant)
    return processed_quadrants

def combine_quadrants(quadrants):
    """Combines the processed quadrants into a single image."""
    height, width = quadrants[0].shape[:2]
    combined_image = np.zeros((height*2, width*2), dtype=np.uint8)
    combined_image[0:height, 0:width] = quadrants[0]
    combined_image[0:height, width:] = quadrants[1]
    combined_image[height:, 0:width] = quadrants[2]
    combined_image[height:, width:] = quadrants[3]
    return combined_image

def save_image(image, path):
    """Saves an image to the specified path."""
    cv2.imwrite(path, image)