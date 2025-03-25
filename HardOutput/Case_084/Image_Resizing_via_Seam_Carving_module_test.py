from Image_Resizing_via_Seam_Carving import resize_image
import numpy as np
from PIL import Image

def test_Image_Resizing_via_Seam_Carving(image_path: str, scale_factor: float, output_path: str) -> None:
    """
    Test the functionality of the Image_Resizing_via_Seam_Carving module.

    Parameters:
    -----------
    image_path : str
        The file path of the input image.
    scale_factor : float
        The factor by which the width of the image should be scaled.
    output_path : str
        The file path where the resized image will be saved.

    Returns:
    --------
    None
    """
    # Load the input image
    image = np.array(Image.open(image_path))

    # Resize the image
    resized_image = resize_image(image, scale_factor)

    # Save the resized image
    Image.fromarray(resized_image).save(output_path)

    # Print success message
    print(f"Resized image saved to {output_path}")

if __name__ == '__main__':
    test_Image_Resizing_via_Seam_Carving("./test_image.png", 1.2, "./test_image_double_size.png")