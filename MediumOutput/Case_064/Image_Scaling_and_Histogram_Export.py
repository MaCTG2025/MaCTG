from load_image import load_image
from scale_image import scale_image
from generate_and_save_histogram import generate_and_save_histogram

def process_image_and_export_histograms(image_path: str) -> None:
    """
    Load an image, scale it up and down by a factor of 2, and export histograms of the original and scaled images.

    Args:
        image_path (str): The path to the input image file (e.g., "./test_image.png").

    Returns:
        None: The function saves histograms of the original, upscaled, and downscaled images as .npy files.

    Example:
        >>> process_image_and_export_histograms("./test_image.png")
        # Saves histograms to "original_hist.npy", "upscaled_hist.npy", and "downscaled_hist.npy"
    """
    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Generate and save histogram for the original image
    generate_and_save_histogram(image, "original_hist.npy")

    # Scale the image up by a factor of 2
    upscaled_image = scale_image(image, 2.0)
    generate_and_save_histogram(upscaled_image, "upscaled_hist.npy")

    # Scale the image down by a factor of 2
    downscaled_image = scale_image(image, 0.5)
    generate_and_save_histogram(downscaled_image, "downscaled_hist.npy")