from PIL import Image
import numpy as np
import cv2

def process_image(image_path: str, circle_radius: int, addition_value: int, subtraction_value: int, output_path: str) -> None:
    """
    Process the input image by applying arithmetic operations to specific regions.

    The function performs the following steps:
    1. Loads the image from the specified `image_path`.
    2. Identifies the central circle region with the given `circle_radius`.
    3. Applies an arithmetic addition operation (pixel-wise) with `addition_value` to the central circle region.
    4. Applies an arithmetic subtraction operation (pixel-wise) with `subtraction_value` to the outer region (outside the central circle).
    5. Saves the processed image to the specified `output_path`.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    circle_radius : int
        The radius of the central circle region in pixels. Must be a positive integer.
    addition_value : int
        The value to add to the pixel values in the central circle region.
    subtraction_value : int
        The value to subtract from the pixel values in the outer region.
    output_path : str
        The file path where the processed image will be saved.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image to `output_path`.

    Requirements:
    -------------
    - The input image must be in a format supported by the PIL library (e.g., PNG, JPEG).
    - The `circle_radius` must be a positive integer.
    - The `addition_value` and `subtraction_value` must be integers.
    - The function assumes the image is large enough to contain the central circle region.

    Example:
    --------
    process_image("./test_image.png", 100, 50, 100, "final_image.png")
    """
    # Load the image
    img = Image.open(image_path)

    # Get image dimensions
    width, height = img.size

    # Create a mask for the central circle
    mask = np.zeros((height, width), dtype=np.uint8)
    circle_center = (width // 2, height // 2)
    cv2.circle(mask, circle_center, circle_radius, 255, -1)


    # Convert image to numpy array for easier manipulation
    img_array = np.array(img)

    # Apply addition to the central circle region
    img_array[mask == 255] = cv2.add(img_array, addition_value)[mask == 255]

    # Apply subtraction to the outer region
    img_array[mask == 0] = cv2.subtract(img_array, subtraction_value)[mask == 0]

    # Ensure pixel values remain within valid range [0, 255]
    img_array = np.clip(img_array, 0, 255)

    # Convert numpy array back to image
    processed_img = Image.fromarray(img_array.astype(np.uint8))

    # Save the processed image
    processed_img.save(output_path)