from Multi_Scale_Template_Matching import multi_scale_template_matching_module

def test_Multi_Scale_Template_Matching(image_path: str, template_path: str, scales: list[float], output_path: str) -> None:
    """
    Test the multi_scale_template_matching_module function to ensure it works as expected.

    Args:
        image_path (str): Path to the input image where the template will be searched.
        template_path (str): Path to the template image that will be matched against the input image.
        scales (list[float]): List of scaling factors to apply to the template (e.g., [0.5, 0.75, 1.25, 1.5]).
        output_path (str): Path where the resulting image with the bounding box will be saved.
    """
    # Call the module function
    multi_scale_template_matching_module(image_path, template_path, scales, output_path)
    print(f"Test completed. Result saved to {output_path}.")

if __name__ == '__main__':
    test_Multi_Scale_Template_Matching(
        image_path="./wheres_waldo.jpg",
        template_path="./waldo_scaled.jpg",
        scales=[0.5, 0.75, 1.25, 1.5],
        output_path="waldo_scaled_image.png"
    )