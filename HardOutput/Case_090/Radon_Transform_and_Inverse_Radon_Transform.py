import numpy as np
from apply_radon_transform import apply_radon_transform
from apply_inverse_radon_transform import apply_inverse_radon_transform

def radon_transform_and_inverse_radon_transform(input_image_path: str, output_radon_path: str, output_inverse_radon_path: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Applies the Radon transform to the input image and then applies the inverse Radon transform to the transformed image.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to which the Radon transform will be applied.
    output_radon_path : str
        The file path where the Radon-transformed image will be saved.
    output_inverse_radon_path : str
        The file path where the inverse Radon-transformed (reconstructed) image will be saved.

    Returns:
    --------
    tuple[np.ndarray, np.ndarray]
        A tuple containing the Radon-transformed image and the inverse Radon-transformed image as numpy arrays.
    """
    # Apply Radon transform
    radon_transformed_image = apply_radon_transform(input_image_path, output_radon_path)
    
    # Apply inverse Radon transform
    inverse_radon_transformed_image = apply_inverse_radon_transform(radon_transformed_image, output_inverse_radon_path)
    
    return radon_transformed_image, inverse_radon_transformed_image