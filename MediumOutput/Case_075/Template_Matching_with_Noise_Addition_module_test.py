from Template_Matching_with_Noise_Addition import template_matching_with_noise_module

def test_template_matching_with_noise_module() -> None:
    """
    Test the functionality of the template_matching_with_noise_module function.
    """
    # Define test input paths and parameters
    input_image_path = "./wheres_waldo.jpg"
    template_image_path = "./waldo.jpg"
    output_image_path = "./wheres_waldo_detected.png"
    sigma = 1.0
    mean = 0.0
    rectangle_thickness = 2

    # Call the module function
    template_matching_with_noise_module(input_image_path, template_image_path, output_image_path, sigma, mean, rectangle_thickness)

    # Print confirmation message
    print("Test completed. Check the output image at:", output_image_path)

if __name__ == '__main__':
    test_template_matching_with_noise_module()