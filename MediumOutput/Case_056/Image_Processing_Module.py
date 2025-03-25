from convert_to_grayscale import convert_to_grayscale
from divide_into_quadrants import divide_into_quadrants
from process_quadrants import process_quadrants
from combine_quadrants import combine_quadrants
from save_image import save_image

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
    """
    # Convert the image to grayscale
    gray_image = convert_to_grayscale(image_path)
    
    # Divide the grayscale image into four quadrants
    quadrants = divide_into_quadrants(gray_image)
    
    # Process each quadrant
    processed_quadrants = process_quadrants(quadrants)
    
    # Combine the processed quadrants into a single image
    combined_image = combine_quadrants(processed_quadrants)
    
    # Save the processed image to the specified output path
    save_image(combined_image, output_path)