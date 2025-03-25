import numpy as np
from PIL import Image
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage.util import img_as_ubyte

def synthesize_texture(input_image_path: str, output_image_path: str, output_size: tuple[int, int]) -> None:
    """
    Synthesizes a texture using the Efros-Leung algorithm and saves the result as an image.

    This function takes an input image, applies the Efros-Leung texture synthesis algorithm to expand it to the specified size,
    and saves the synthesized texture as a new image file. The random seed is set to 0 to ensure reproducibility.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./texture_icon.jpg").
    output_image_path : str
        The file path where the synthesized texture will be saved (e.g., "texture_synthesized.png").
    output_size : tuple[int, int]
        The desired size of the output image as a tuple of (width, height) in pixels (e.g., (128, 128)).

    Returns:
    --------
    None
        The function does not return any value. The synthesized texture is saved directly to the specified output path.

    Requirements:
    -------------
    1. The input image must exist at the specified path.
    2. The output image path must be writable.
    3. The output_size must be a tuple of two positive integers.
    4. The random seed is set to 0 before starting the algorithm to ensure reproducibility.

    Example:
    --------
    synthesize_texture("./texture_icon.jpg", "texture_synthesized.png", (128, 128))
    """
    # Load the input image
    input_image = Image.open(input_image_path)
    input_array = np.array(input_image)

    # Set the random seed for reproducibility
    np.random.seed(0)

    # Initialize the output array with zeros
    output_array = np.zeros((output_size[1], output_size[0], input_array.shape[2]), dtype=np.uint8)

    # Define the neighborhood size
    neighborhood_size = 3

    # Iterate over each pixel in the output array
    for y in range(output_size[1]):
        for x in range(output_size[0]):
            # Get the patch from the input image
            patch_y = max(0, min(y - neighborhood_size // 2, input_array.shape[0] - neighborhood_size))
            patch_x = max(0, min(x - neighborhood_size // 2, input_array.shape[1] - neighborhood_size))
            patch = input_array[patch_y:patch_y + neighborhood_size, patch_x:patch_x + neighborhood_size]

            # Choose a random pixel from the patch
            random_index = np.random.randint(patch.shape[0])
            random_pixel = patch[random_index, random_index]

            # Assign the random pixel to the output array
            output_array[y, x] = random_pixel

    # Convert the output array to an image and save it
    output_image = Image.fromarray(img_as_ubyte(output_array))
    output_image.save(output_image_path)