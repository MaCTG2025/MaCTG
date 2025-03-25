from Template Matching with Noise Addition import template_matching_with_noise_module

def main() -> None:
    """
    Entry point for the project. Calls the template matching with noise addition function
    to process the input image, locate the template, and save the output image.
    """
    template_matching_with_noise_module(
        input_image_path="./wheres_waldo.jpg",
        template_image_path="./waldo.jpg",
        output_image_path="wheres_waldo_detected.png",
        sigma=1.0,
        mean=0.0,
        rectangle_thickness=2
    )

if __name__ == '__main__':
    main()