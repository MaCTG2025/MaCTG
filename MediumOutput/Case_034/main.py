from load_and_validate_image import load_and_validate_image
from apply_circular_mask_and_blur import apply_circular_mask_and_blur
from save_processed_image import save_processed_image

def process_image_with_mask_and_blur(image_path: str, output_path: str, radius: int, kernel_size: int, sigmaX: int) -> None:
    """
    Load an image, apply a circular mask and Gaussian blur outside the mask, and save the processed image.

    Args:
        image_path (str): The file path to the input image.
        output_path (str): The file path where the processed image will be saved.
        radius (int): The radius of the circular mask in pixels.
        kernel_size (int): The size of the Gaussian kernel (must be an odd integer).
        sigmaX (int): The standard deviation of the Gaussian kernel in the X direction.

    Returns:
        None: The function saves the processed image to disk and does not return any value.

    Raises:
        ValueError: If the image cannot be loaded, processed, or saved.
    """
    image = load_and_validate_image(image_path)
    processed_image = apply_circular_mask_and_blur(image, radius, kernel_size, sigmaX)
    save_processed_image(processed_image, output_path)

if __name__ == '__main__':
    process_image_with_mask_and_blur('./test_image.png', 'final_image.png', 100, 15, 10)