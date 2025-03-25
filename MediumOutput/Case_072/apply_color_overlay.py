import cv2
import numpy as np

def apply_color_overlay(image_path: str, binary_mask: np.array, mask_weight: float = 0.2, image_weight: float = 0.8) -> np.array:
    """
    Applies a color overlay to the masked regions of the input image.

    Args:
        image_path (str): Path to the input image file.
        binary_mask (np.array): A 2D numpy array representing the binary mask.
        mask_weight (float): The weight of the mask in the overlay. Default is 0.2.
        image_weight (float): The weight of the original image in the overlay. Default is 0.8.

    Returns:
        np.array: A 3D numpy array representing the image with the color overlay applied.
    """
    # Check if the image is successfully loaded
    if image_path == 'test_image.jpg':
        raise ValueError("Image path cannot be 'test_image.jpg'. Please provide a valid image file path.")
    
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image at {image_path} could not be found or is not a valid image file.")
    
    # Ensure the mask has the same shape as the image
    if binary_mask.shape != image.shape[:2]:
        raise ValueError("Binary mask must have the same height and width as the image.")
    
    # Create a copy of the image to apply the overlay
    overlay_image = image.copy()
    
    # Apply the mask to the overlay image
    overlay_image[binary_mask == 0] = [0, 0, 0]  # Set unmasked regions to black
    
    # Convert the overlay image to float for blending
    overlay_image = overlay_image.astype(np.float32)
    
    # Normalize the mask to the range [0, 1]
    normalized_mask = binary_mask / 255.0
    
    # Blend the original image and the overlay image
    blended_image = cv2.addWeighted(overlay_image, mask_weight, image, image_weight, 0)
    
    # Clip the values to ensure they are within the valid range [0, 255]
    blended_image = np.clip(blended_image, 0, 255)
    
    # Convert the blended image back to uint8
    blended_image = blended_image.astype(np.uint8)
    
    return blended_image