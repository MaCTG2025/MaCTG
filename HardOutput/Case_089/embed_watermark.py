import cv2
import numpy as np
from PIL import Image, ImageDraw
import pywt

def embed_watermark(input_image_path: str, output_image_path: str) -> None:
    """
    Embeds a star-shaped watermark into an input image in the frequency domain using Discrete Wavelet Transform (DWT).

    The function performs the following steps:
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

    Requirements:
    -------------
    - The input image must be in a format supported by OpenCV (e.g., PNG, JPEG).
    - The watermark is generated as a star shape using PIL (Python Imaging Library).
    - The watermark embedding process must be robust and preserve the visual quality of the image.
    - The function must handle grayscale and color images appropriately.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing.
    - NumPy (numpy) for numerical operations.
    - PIL (Pillow) for generating the star-shaped watermark.

    Example:
    --------
    embed_watermark("./test_image.png", "./watermarked_image.png")
    """
    # Read the input image
    img = cv2.imread(input_image_path)
    
    # Convert the image into yuv color space and extract the Y channel
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_gray = img_yuv[:, :, 0]
    
    # Generate a star-shaped watermark
    watermark_size = min(img_gray.shape[:2])
    mask = np.zeros((watermark_size, watermark_size), dtype=np.uint8)
    center = (watermark_size // 2, watermark_size // 2)
    radius = watermark_size // 4
    points = [center]
    for i in range(5):
        angle = 2 * np.pi * i / 5 + np.pi / 10
        x = int(center[0] + radius * np.cos(angle))
        y = int(center[1] + radius * np.sin(angle))
        points.append((x, y))
    cv2.fillPoly(mask, [np.array(points)], 255)
    mask = cv2.resize(mask, (img_gray.shape[1], img_gray.shape[0]))
    
    # Apply DWT to decompose the image
    coeffs = pywt.wavedec2(img_gray, 'haar', level=1)
    
    # Embed the watermark into the frequency domain
    mask = cv2.resize(mask, (coeffs[0].shape[1], coeffs[0].shape[0]))
    mask = mask / 255.0
    coeffs[0] += mask

    # Reconstruct the image using IDWT
    watermarked_img = pywt.waverec2(coeffs, 'haar')

    # Clip the pixel values to be within the valid range [0, 255]
    watermarked_img = np.clip(watermarked_img, 0, 255).astype(np.uint8)

    # Convert the image back to BGR color space
    img_yuv[:, :, 0] = watermarked_img
    watermarked_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    
    # Save the watermarked image
    cv2.imwrite(output_image_path, watermarked_img)