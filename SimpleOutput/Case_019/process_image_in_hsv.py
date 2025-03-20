import cv2
import os

def process_image_in_hsv(input_image_path: str) -> None:
    """
    Converts an input image to the HSV color space, splits it into Hue, Saturation, and Value channels,
    and saves the HSV image and the three channels as separate files.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the following files to disk:
        - "HSV.png": The image converted to the HSV color space.
        - "hue_channel.png": The Hue channel of the HSV image.
        - "saturation_channel.png": The Saturation channel of the HSV image.
        - "value_channel.png": The Value channel of the HSV image.

    Requirements:
    -------------
    1. The input image must exist at the specified path.
    2. The function uses OpenCV (cv2) for image processing, so ensure OpenCV is installed.
    3. The output files will be saved in the same directory as the input image.

    Example:
    --------
    process_image_in_hsv("./test_image.png")
    """
    # Load the image from the given path
    image = cv2.imread(input_image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the HSV image into its constituent channels
    hue_channel, saturation_channel, value_channel = cv2.split(hsv_image)

    # Define the output file paths
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    output_dir = os.path.dirname(input_image_path)
    hsv_output_path = os.path.join(output_dir, f"HSV.png")
    hue_output_path = os.path.join(output_dir, f"hue_channel.png")
    saturation_output_path = os.path.join(output_dir, f"saturation_channel.png")
    value_output_path = os.path.join(output_dir, f"value_channel.png")

    # Save the HSV image and each channel as separate files
    cv2.imwrite(hsv_output_path, hsv_image)
    cv2.imwrite(hue_output_path, hue_channel)
    cv2.imwrite(saturation_output_path, saturation_channel)
    cv2.imwrite(value_output_path, value_channel)