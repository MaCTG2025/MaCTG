from watershed_segmentation import watershed_segmentation

def watershed_image_segmentation(input_image_path: str, output_image_path: str) -> None:
    """
    Perform image segmentation using the Watershed method on the input image and save the result.

    This module-level function uses the `watershed_segmentation` function to segment an image
    into distinct regions based on intensity gradients and saves the segmented image to the
    specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./water_coins.jpg").
    output_image_path : str
        The file path where the segmented image will be saved (e.g., "water_coins_segmented.png").

    Returns:
    --------
    None
        The function does not return any value. It saves the segmented image to the specified output path.

    Example:
    --------
    watershed_image_segmentation("./water_coins.jpg", "water_coins_segmented.png")
    """
    watershed_segmentation(input_image_path, output_image_path)

if __name__ == '__main__':
    watershed_image_segmentation("./water_coins.jpg", "water_coins_segmented.png")