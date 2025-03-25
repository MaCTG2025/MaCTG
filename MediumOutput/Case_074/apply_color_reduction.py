import numpy as np
from PIL import Image

def apply_color_reduction(regions: list, color_levels: list, output_path: str) -> None:
    """
    Applies fixed-level color reduction to each region using specified color levels, combines the regions,
    and saves the final image.

    Args:
        regions (list): A list of four NumPy arrays, each representing one of the four equal regions of the image.
        color_levels (list): A list of four integers specifying the number of color levels to apply to each region.
                             The order of color levels corresponds to the order of regions:
                             [top-left, top-right, bottom-left, bottom-right].
        output_path (str): The file path where the final image will be saved (e.g., "color_reduction.png").

    Returns:
        None: The function does not return any value. It saves the final image to the specified output path.

    Requirements:
        - The `regions` list must contain exactly four NumPy arrays.
        - The `color_levels` list must contain exactly four integers, each representing the number of color levels
          to apply to the corresponding region.
        - The `output_path` must be a valid file path with a supported image format (e.g., PNG, JPEG).
        - The function should handle the color reduction process for each region independently and combine the
          regions into a single image before saving.
        - If the number of regions or color levels is not exactly four, the function should raise a ValueError.
    """
    if len(regions) != 4 or len(color_levels) != 4:
        raise ValueError("The regions list must contain exactly four NumPy arrays and the color_levels list must contain exactly four integers.")

    combined_image = np.vstack((np.hstack((regions[0], regions[1])), np.hstack((regions[2], regions[3]))))

    reduced_images = []
    for i, region in enumerate(regions):
        max_value = 255
        step = max_value // color_levels[i]
        reduced_region = np.clip(region // step, 0, color_levels[i] - 1) * step
        reduced_images.append(reduced_region)

    reduced_combined_image = np.vstack((np.hstack((reduced_images[0], reduced_images[1])), np.hstack((reduced_images[2], reduced_images[3]))))

    img = Image.fromarray(reduced_combined_image.astype(np.uint8))
    img.save(output_path)