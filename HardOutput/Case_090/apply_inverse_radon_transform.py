import numpy as np
from skimage.transform import iradon
from skimage.io import imsave
from skimage import exposure

def apply_inverse_radon_transform(radon_transformed_image: np.ndarray, output_image_path: str) -> np.ndarray:
    """
    Applies the inverse Radon transform to the Radon-transformed image and saves the reconstructed image.

    Parameters:
    -----------
    radon_transformed_image : np.ndarray
        A 2D numpy array representing the Radon-transformed image.
    
    output_image_path : str
        The file path where the inverse Radon-transformed (reconstructed) image will be saved.
        The output image will be saved in a format supported by `skimage.io.imsave`.

    Returns:
    --------
    np.ndarray
        A 2D numpy array representing the inverse Radon-transformed (reconstructed) image.
    """
    # Apply the inverse Radon transform using filtered back-projection
    reconstructed_image = iradon(radon_transformed_image, circle=True)
    
    reconstructed_normalized = exposure.rescale_intensity(reconstructed_image, out_range=(0, 255)).astype(np.uint8)
    imsave("Inverse_Radon_transformed_Phantom.png", reconstructed_normalized)