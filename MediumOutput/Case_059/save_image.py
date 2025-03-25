from PIL import Image
import numpy as np

def save_image(segmented_image: np.array, output_path: str) -> None:
    """
    Save the segmented image to the specified output file path.

    Args:
        segmented_image (np.array): The segmented image as a NumPy array with shape (height, width, channels).
        output_path (str): The file path where the segmented image will be saved.

    Raises:
        ValueError: If the input image is not a valid NumPy array.
        IOError: If the file cannot be saved at the specified output path.
    """
    if not isinstance(segmented_image, np.ndarray):
        raise ValueError("The input image must be a NumPy array.")
    
    try:
        image = Image.fromarray(segmented_image)
        image.save(output_path, 'PNG')
    except IOError as e:
        raise IOError(f"Failed to save the image to {output_path}: {e}")