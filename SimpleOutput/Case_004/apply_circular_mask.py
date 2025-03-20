from PIL import Image, ImageDraw

def apply_circular_mask(input_image_path: str, output_image_path: str, mask_radius: int) -> None:
    """
    Applies a circular mask to an input image and saves the result.

    The function reads an image from the specified input path, creates a circular mask centered at the image's center,
    and applies the mask to the image. The resulting image is saved to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the masked image will be saved (e.g., "masked_image.png").
    mask_radius : int
        The radius of the circular mask in pixels (e.g., 100).

    Returns:
    --------
    None
        The function does not return any value. It saves the resulting image to the specified output path.

    Requirements:
    -------------
    - The input image must exist at the specified path.
    - The mask will be a white circle with the given radius, centered at the image's center.
    - Pixels outside the circle will be black.
    - The output image will be saved in the same format as the input image.

    Example:
    --------
    apply_circular_mask("./test_image.png", "masked_image.png", 100)
    """
    # Open the input image
    img = Image.open(input_image_path)
    width, height = img.size
    
    # Create a new image for the mask
    mask = Image.new('L', (width, height), 0)
    
    # Draw the circular mask
    draw = ImageDraw.Draw(mask)
    draw.ellipse((width//2-mask_radius, height//2-mask_radius, width//2+mask_radius, height//2+mask_radius), fill=255)
    
    # Apply the mask to the original image
    img.putalpha(mask)
    
    # Save the resulting image
    img.save(output_image_path)