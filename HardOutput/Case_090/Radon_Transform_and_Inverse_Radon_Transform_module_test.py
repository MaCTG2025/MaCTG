import numpy as np
from Radon_Transform_and_Inverse_Radon_Transform import radon_transform_and_inverse_radon_transform

def test_Radon_Transform_and_Inverse_Radon_Transform(input_image_path: str, output_radon_path: str, output_inverse_radon_path: str) -> None:
    """
    Tests the functionality of the Radon_Transform_and_Inverse_Radon_Transform module.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to which the Radon transform will be applied.
    output_radon_path : str
        The file path where the Radon-transformed image will be saved.
    output_inverse_radon_path : str
        The file path where the inverse Radon-transformed (reconstructed) image will be saved.
    """
    # Call the module function
    radon_image, inverse_radon_image = radon_transform_and_inverse_radon_transform(input_image_path, output_radon_path, output_inverse_radon_path)
    
    # Check output types
    assert isinstance(radon_image, np.ndarray), "Radon-transformed image is not a numpy array."
    assert isinstance(inverse_radon_image, np.ndarray), "Inverse Radon-transformed image is not a numpy array."
    
    # Check output shapes (basic validation)
    assert len(radon_image.shape) == 2, "Radon-transformed image is not a 2D array."
    assert len(inverse_radon_image.shape) == 2, "Inverse Radon-transformed image is not a 2D array."
    
    print("Test passed: Output types and shapes are correct.")

if __name__ == '__main__':
    test_Radon_Transform_and_Inverse_Radon_Transform("./Phantom.png", "Radon_transformed_Phantom.png", "Inverse_Radon_transformed_Phantom.png")