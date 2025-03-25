from PIL import Image
import numpy as np

def apply_dynamic_color_filter(image_path: str, brightness_threshold: int = 150) -> None:
    """
    Processes an input image by applying dynamic color filtering based on pixel brightness.
    Converts regions with pixel brightness above a specified threshold to grayscale, while
    leaving the rest of the image unchanged. The processed image is saved as 'filtered_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed. The image should be in a format
        supported by the PIL library (e.g., PNG, JPEG).

    brightness_threshold : int, optional (default=150)
        The brightness threshold value. Pixels with brightness above this value will be
        converted to grayscale. The brightness is calculated as the average of the RGB values.

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved as 'filtered_image.png'
        in the current working directory.

    Requirements:
    -------------
    1. The function uses the PIL (Pillow) library to handle image processing.
    2. The function uses NumPy for efficient pixel brightness calculations.
    3. The input image must be in a format supported by PIL (e.g., PNG, JPEG).
    4. The brightness threshold must be an integer between 0 and 255.

    Example:
    --------
    apply_dynamic_color_filter("./test_image.png", brightness_threshold=150)
    """
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)
    
    # Calculate the brightness of each pixel
    brightness = np.mean(img_array, axis=2)
    
    # Create a mask where pixels are brighter than the threshold
    mask = brightness > brightness_threshold
    
    # Apply the mask to convert bright pixels to grayscale
    grayscale = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    img_array[mask] = np.stack([grayscale[mask]] * 3, axis=-1).astype(np.uint8)
    
    # Convert the NumPy array back to a PIL image
    filtered_img = Image.fromarray(img_array)
    
    # Save the filtered image
    filtered_img.save('filtered_image.png')