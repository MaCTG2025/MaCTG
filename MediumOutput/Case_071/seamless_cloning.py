import cv2
import numpy as np

def seamless_cloning(background_image: np.ndarray, transformed_object_image: np.ndarray) -> np.ndarray:
    """
    Place the transformed object image onto the center of the background image using seamless cloning (Poisson blending).

    Args:
        background_image (np.ndarray): The background image as a NumPy array.
        transformed_object_image (np.ndarray): The transformed object image as a NumPy array.

    Returns:
        np.ndarray: The final blended image as a NumPy array.

    Requirements:
        - The transformed object image should be placed at the center of the background image.
        - Seamless cloning should be performed using Poisson blending to ensure smooth integration.
        - The function should handle cases where the object image is larger than the background image.
    """
    # Calculate the center position for placing the object image
    bg_height, bg_width = background_image.shape[:2]
    obj_height, obj_width = transformed_object_image.shape[:2]

    # Resize the object image if it is larger than the background image
    if obj_height > bg_height or obj_width > bg_width:
        scale_factor = min(bg_height / obj_height, bg_width / obj_width)
        transformed_object_image = cv2.resize(transformed_object_image, None, fx=scale_factor, fy=scale_factor)

    # Calculate the new dimensions after resizing
    obj_height, obj_width = transformed_object_image.shape[:2]

    x_offset = (bg_width - obj_width) // 2
    y_offset = (bg_height - obj_height) // 2

    # Create a mask for the object image
    mask = np.ones(transformed_object_image.shape[:2], dtype=np.uint8) * 255

    print(transformed_object_image.shape)
    print(background_image.shape)
    # Perform seamless cloning
    blended_image = cv2.seamlessClone(
        transformed_object_image, background_image,
        mask, (x_offset + obj_width // 2, y_offset + obj_height // 2),
        cv2.NORMAL_CLONE
    )

    return blended_image