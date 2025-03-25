import numpy as np

def calculate_and_save_differences(rescaled_images: dict) -> None:
    """
    Calculate the pixel intensity differences between pairs of rescaled images and save the results as .npy files.

    Args:
        rescaled_images (dict): A dictionary containing rescaled images with keys as interpolation method names.
            Example: {'Linear': linear_image, 'Cubic': cubic_image, 'Area': area_image}.

    Returns:
        None: The function saves the following .npy files:
            - "diff_linear_cubic.npy": Pixel intensity differences between Linear and Cubic rescaled images.
            - "diff_cubic_area.npy": Pixel intensity differences between Cubic and Area rescaled images.
            - "diff_area_linear.npy": Pixel intensity differences between Area and Linear rescaled images.

    Requirements:
        - The input dictionary must contain exactly three rescaled images with keys 'Linear', 'Cubic', and 'Area'.
        - The rescaled images must be of the same dimensions.
        - The function will raise a ValueError if the dictionary does not contain the required keys.
        - The function will raise a ValueError if the rescaled images are not of the same dimensions.

    Example:
        >>> calculate_and_save_differences({'Linear': linear_image, 'Cubic': cubic_image, 'Area': area_image})
    """
    required_keys = {'Linear', 'Cubic', 'Area'}
    if required_keys != set(rescaled_images.keys()):
        raise ValueError("The dictionary must contain exactly three rescaled images with keys 'Linear', 'Cubic', and 'Area'.")

    for key in required_keys:
        if not isinstance(rescaled_images[key], np.ndarray):
            raise ValueError(f"The values associated with keys '{key}' must be numpy arrays.")

    if not all(rescaled_images['Linear'].shape == img.shape for img in rescaled_images.values()):
        raise ValueError("All rescaled images must be of the same dimensions.")

    diff_linear_cubic = rescaled_images['Linear'].astype(np.int16) - rescaled_images['Cubic'].astype(np.int16)
    diff_cubic_area = rescaled_images['Cubic'].astype(np.int16) - rescaled_images['Area'].astype(np.int16)
    diff_area_linear = rescaled_images['Area'].astype(np.int16) - rescaled_images['Linear'].astype(np.int16)

    np.save('diff_linear_cubic.npy', diff_linear_cubic)
    np.save('diff_cubic_area.npy', diff_cubic_area)
    np.save('diff_area_linear.npy', diff_area_linear)