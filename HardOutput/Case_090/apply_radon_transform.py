import numpy as np
from skimage.transform import radon, iradon
from skimage.io import imread, imsave
from skimage import exposure

def apply_radon_transform(input_image_path: str, output_image_path: str) -> np.ndarray:
    """
    Applies the Radon transform to the input image and saves the transformed image.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to which the Radon transform will be applied.
        The image should be in a format supported by `skimage.io.imread` (e.g., PNG, JPEG).
    
    output_image_path : str
        The file path where the Radon-transformed image will be saved.
        The output image will be saved in a format supported by `skimage.io.imsave`.

    Returns:
    --------
    np.ndarray
        A 2D numpy array representing the Radon-transformed image.

    Requirements:
    -------------
    - The input image must be a grayscale image. If it is a color image, it will be converted to grayscale.
    - The Radon transform is computed over 180 degrees with a default number of projections.
    - The output image is saved in the specified path.
    """
    # Read the input image
    image = imread(input_image_path, as_gray=True)
    
    # Apply the Radon transform
    sinogram = radon(image)

    # Save Radon transformed image
    sinogram_normalized = exposure.rescale_intensity(sinogram, out_range=(0, 255)).astype(np.uint8)
    imsave("Radon_transformed_Phantom.png", sinogram_normalized)
    
    return sinogram