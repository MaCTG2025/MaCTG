from load_image import load_image
from convert_to_grayscale import convert_to_grayscale
from apply_threshold import apply_threshold
from apply_gaussian_blur import apply_gaussian_blur
from combine_images import combine_images
from save_image import save_image

def process_image(image_path: str, output_path: str, threshold_value: int = 200, kernel_size: tuple = (5, 5)) -> None:
    """
    Process an image by converting it to grayscale, applying a brightness threshold, blurring bright regions,
    combining the results, and saving the final image.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the final image will be saved.
        threshold_value (int): The brightness threshold value (0-255). Default is 200.
        kernel_size (tuple): The size of the Gaussian kernel. Default is (5, 5).

    Returns:
        None
    """
    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Convert to grayscale
    grayscale_image = convert_to_grayscale(image)
    if grayscale_image is None:
        return

    # Apply threshold
    binary_mask = apply_threshold(grayscale_image, threshold_value)
    if binary_mask is None:
        return

    # Apply Gaussian blur to bright regions
    blurred_image = apply_gaussian_blur(grayscale_image, binary_mask, kernel_size)
    if blurred_image is None:
        return

    # Combine blurred bright regions with original dark regions
    final_image = combine_images(blurred_image, grayscale_image, binary_mask)
    if final_image is None:
        return

    # Save the final image
    save_image(final_image, output_path)

if __name__ == '__main__':
    process_image('./test_image.png', 'bright_regions.png')