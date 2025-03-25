from PIL import Image
import numpy as np

def scale_image(image: np.array, scale_factor: float) -> np.array:
    """
    Scale the input image by a given factor using bilinear interpolation.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).
        scale_factor (float): The scaling factor.
            - If scale_factor > 1, the image will be upscaled.
            - If scale_factor < 1, the image will be downscaled.

    Returns:
        np.array: The scaled image as a NumPy array with shape (new_height, new_width, channels).

    Requirements:
        - The input image must be a valid NumPy array.
        - The scaling factor must be a positive float.
        - The function should handle both upscaling and downscaling.
        - The function should preserve the aspect ratio of the image.

    Example:
        >>> scaled_image = scale_image(image, 2.0)  # Upscale by a factor of 2
        >>> print(scaled_image.shape)
        (960, 1280, 3)
    """
    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(image)

    # Calculate the new size while preserving the aspect ratio
    original_width, original_height = pil_image.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Resize the image using bilinear interpolation
    resized_pil_image = pil_image.resize((new_width, new_height), Image.BILINEAR)

    # Convert the resized PIL Image back to a NumPy array
    scaled_image = np.array(resized_pil_image)

    return scaled_image