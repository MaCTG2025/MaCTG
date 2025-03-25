from divide_image import divide_image
from apply_color_reduction import apply_color_reduction
import numpy as np

def process_image_color_reduction(image_path: str, color_levels: list, output_path: str) -> None:
    """
    Processes an image by dividing it into four equal regions, applying fixed-level color reduction to each region,
    and saving the final image.

    Args:
        image_path (str): The file path of the input image.
        color_levels (list): A list of four integers specifying the number of color levels to apply to each region.
                             The order of color levels corresponds to the order of regions:
                             [top-left, top-right, bottom-left, bottom-right].
        output_path (str): The file path where the final image will be saved (e.g., "color_reduction.png").

    Returns:
        None: The function does not return any value. It saves the final image to the specified output path.
    """
    # Load the image
    image = np.array(Image.open(image_path))
    
    # Divide the image into four regions
    regions = divide_image(image)
    
    # Apply color reduction to each region and save the final image
    apply_color_reduction(regions, color_levels, output_path)