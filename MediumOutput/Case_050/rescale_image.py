from PIL import Image
import numpy as np

def rescale_image(image: np.array, interpolation_method: str, scale_factor: float) -> np.array:
    """
    Rescale the input image using the specified interpolation method.

    Args:
        image (np.array): The input image as a NumPy array.
        interpolation_method (str): The interpolation method to use for rescaling.
            Supported methods: 'BILINEAR', 'BICUBIC', 'BOX'.
        scale_factor (float): The factor by which to scale the image.
            Example: 0.5 for halving the size, 2.0 for doubling the size.

    Returns:
        np.array: The rescaled image as a NumPy array.

    Raises:
        ValueError: If the interpolation method is unsupported.
        ValueError: If the scale factor is not positive.
    """
    if interpolation_method not in ['BILINEAR', 'BICUBIC', 'BOX']:
        raise ValueError("Unsupported interpolation method")
    
    if scale_factor <= 0:
        raise ValueError("Scale factor must be positive")

    pil_image = Image.fromarray(image)
    new_size = tuple(int(dim * scale_factor) for dim in pil_image.size)
    rescaled_pil_image = pil_image.resize(new_size, getattr(Image.Resampling, interpolation_method))
    rescaled_image = np.array(rescaled_pil_image)

    return rescaled_image