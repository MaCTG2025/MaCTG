from load_image import load_image
from apply_affine_transform import apply_affine_transform
from harris_corner_detection import harris_corner_detection
from save_image import save_image

def process_image(image_path: str) -> None:
    """
    Main function that orchestrates the entire process:
    - Load the image from the specified path.
    - Apply an affine transformation (45° rotation, 1.2x scaling, and translation by (50, 30) pixels).
    - Perform Harris corner detection on both the original and transformed images.
    - Save the resulting images as "harris_original.png" and "harris_transformed.png".

    Args:
        image_path (str): The file path of the input image.

    Returns:
        None

    Example:
        >>> process_image("./test_image.png")
    """
    # Load the image
    img = load_image(image_path)
    
    # Apply affine transformation
    img_transformed = apply_affine_transform(img)
    
    # Perform Harris corner detection on the original image
    img_with_corners = harris_corner_detection(img)
    
    # Perform Harris corner detection on the transformed image
    img_transformed_with_corners = harris_corner_detection(img_transformed)
    
    # Save the resulting images
    save_image(img_with_corners, "harris_original.png")
    save_image(img_transformed_with_corners, "harris_transformed.png")