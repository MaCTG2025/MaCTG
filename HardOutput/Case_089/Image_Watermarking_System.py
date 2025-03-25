from embed_watermark import embed_watermark

def image_watermarking_system(input_image_path: str, output_image_path: str) -> None:
    """
    Embeds a star-shaped watermark into an input image in the frequency domain using Discrete Wavelet Transform (DWT).

    This module-level function performs the following steps:
    1. Reads the input image from the specified path.
    2. Generates a star-shaped watermark.
    3. Converts the image and watermark to grayscale if they are not already.
    4. Applies Discrete Wavelet Transform (DWT) to decompose the image into frequency sub-bands.
    5. Embeds the watermark into the frequency domain of the image.
    6. Reconstructs the image using Inverse Discrete Wavelet Transform (IDWT).
    7. Saves the watermarked image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the watermarked image will be saved (e.g., "./watermarked_image.png").

    Returns:
    --------
    None
        The function does not return any value. The watermarked image is saved to the specified output path.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing.
    - NumPy (numpy) for numerical operations.
    - PIL (Pillow) for generating the star-shaped watermark.
    - PyWavelets (pywt) for Discrete Wavelet Transform (DWT) operations.
    """
    embed_watermark(input_image_path, output_image_path)