from .utils import load_image, rotate_image, compute_gradient_magnitude, compare_gradients, generate_heatmap

def process_image(image_path: str, output_path: str) -> None:
    """
    A single function that combines all the above steps to process the image, compute gradients,
    compare them, and generate the heatmap.

    Args:
        image_path (str): The file path to the input image.
        output_path (str): The file path where the heatmap image will be saved.

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the image format is not supported by OpenCV.
        IOError: If the output file path is invalid or inaccessible.

    Requirements:
        - The input image must be loaded using the `load_image` function.
        - The image must be rotated using the `rotate_image` function.
        - The gradient magnitudes of the original and rotated images must be computed using the `compute_gradient_magnitude` function.
        - The gradient magnitudes must be compared using the `compare_gradients` function.
        - The heatmap must be generated and saved using the `generate_heatmap` function.
    """
    # Load the image
    image = load_image(image_path)

    # Rotate the image
    rotated_image = rotate_image(image)

    # Compute gradient magnitudes
    original_grad_magnitude = compute_gradient_magnitude(image)
    rotated_grad_magnitude = compute_gradient_magnitude(rotated_image)

    # Compare gradients
    comparison_result = compare_gradients(original_grad_magnitude, rotated_grad_magnitude)

    # Generate heatmap
    heatmap = generate_heatmap(comparison_result, output_path)