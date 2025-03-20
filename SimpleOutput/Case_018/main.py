from detect_shapes import detect_shapes
from draw_and_save_contours import draw_and_save_contours

def process_image_with_shapes(image_path: str, output_path: str) -> None:
    """
    Detects shapes in the input image, draws their contours with specified colors, and saves the output image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the output image file.

    Returns:
        None: The function saves the output image to the specified path.

    Steps:
        1. Detect shapes in the input image using `detect_shapes`.
        2. Draw contours of the detected shapes with predefined colors and thickness using `draw_and_save_contours`.
        3. Save the resulting image to the specified output path.
    """
    # Define colors for each shape
    colors = {
        'rectangle': (0, 0, 255),  # Red
        'square': (0, 255, 0),     # Green
        'triangle': (255, 0, 0),   # Blue
        'circle': (0, 255, 255),   # Yellow
        'star': (255, 0, 255)      # Pink
    }

    # Detect shapes in the image
    shapes = detect_shapes(image_path)

    # Draw contours and save the output image
    draw_and_save_contours(image_path, shapes, colors, thickness=2, output_path=output_path)

if __name__ == '__main__':
    process_image_with_shapes('./someshapes.jpg', 'shapes_image.png')