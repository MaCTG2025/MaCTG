from adjust_brightness import adjust_brightness
from perform_template_matching import perform_template_matching
from draw_rectangle_and_save import draw_rectangle_and_save

def find_and_highlight_waldo(image_path: str, template_path: str, output_path: str) -> None:
    """
    Finds Waldo in the given image using template matching, highlights the matched region,
    and saves the resulting image.

    Args:
        image_path (str): Path to the input image file (e.g., "./wheres_waldo.jpg").
        template_path (str): Path to the template image file (e.g., "./waldo.jpg").
        output_path (str): Path to save the resulting image (e.g., "wheres_waldo_matched.png").

    Returns:
        None: The function saves the image to disk and does not return anything.
    """
    brightened_image = adjust_brightness(image_path)
    matched_region = perform_template_matching(brightened_image, template_path)
    draw_rectangle_and_save(brightened_image, matched_region, output_path)

if __name__ == '__main__':
    find_and_highlight_waldo("./wheres_waldo.jpg", "./waldo.jpg", "wheres_waldo_matched.png")