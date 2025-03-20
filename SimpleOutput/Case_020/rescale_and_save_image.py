import cv2

def rescale_and_save_image(input_image_path: str) -> None:
    """
    Loads an image from the specified path, rescales it to twice its original size using Linear, Cubic, and Area Interpolation,
    and saves the resulting images to disk.

    Args:
        input_image_path (str): The file path to the input image that needs to be rescaled. 
                               Example: "./test_image.png"

    Returns:
        None: This function does not return any value. It saves the rescaled images to disk with the following filenames:
              - "linear_interpolation.png" (rescaled using Linear Interpolation)
              - "cubic_interpolation.png" (rescaled using Cubic Interpolation)
              - "area_interpolation.png" (rescaled using Area Interpolation)

    Requirements:
        1. The input image must exist at the specified path; otherwise, the function will raise an error.
        2. The function uses OpenCV's `cv2.resize` method with the following interpolation methods:
           - Linear Interpolation: `cv2.INTER_LINEAR`
           - Cubic Interpolation: `cv2.INTER_CUBIC`
           - Area Interpolation: `cv2.INTER_AREA`
        3. The rescaled images are saved in the same directory as the input image.

    Example Usage:
        rescale_and_save_image("./test_image.png")
    """
    # Load the image
    image = cv2.imread(input_image_path)
    
    # Check if image is loaded properly
    if image is None:
        raise ValueError("Image not found at the specified path.")
    
    # Define the scale factor
    scale_factor = 2
    
    # Rescale the image using different interpolation methods
    linear_resized = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    cubic_resized = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    area_resized = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    
    # Save the rescaled images
    cv2.imwrite("linear_interpolation.png", linear_resized)
    cv2.imwrite("cubic_interpolation.png", cubic_resized)
    cv2.imwrite("area_interpolation.png", area_resized)