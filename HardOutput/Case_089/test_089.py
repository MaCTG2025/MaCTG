'''
Given an input image ("./test_image.png"), create a star-shape watermark and create a robust image watermarking system that embeds a watermark in the frequency domain using Discrete Wavelet Transform (DWT). Save the watermarked image as "./watermarked_image.png".
'''

import cv2
import numpy as np
import pywt
import os


def load_image(image_path: str) -> np.ndarray:
    image = cv2.imread(image_path)
    return image


def create_star_shape_watermark(size: int) -> np.ndarray:
    watermark = np.zeros((size, size), dtype=np.uint8)
    center = (size // 2, size // 2)
    cv2.ellipse(watermark, center, (size // 2, size // 4), 0, 0, 360, 255, -1)
    cv2.ellipse(watermark, center, (size // 4, size // 2), 0, 0, 360, 255, -1)
    return watermark


def embed_watermark_dwt(image: np.ndarray, watermark: np.ndarray) -> np.ndarray:
    # Convert the image to YUV color space
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # Extract the Y channel
    y_channel = yuv_image[:, :, 0]

    # Perform DWT on the Y channel
    coeffs = pywt.dwt2(y_channel, 'haar')

    # Extract LL, (LH, HL, HH)
    LL, (LH, HL, HH) = coeffs

    # Resize watermark to match the LL sub-band size
    resized_watermark = cv2.resize(watermark, (LL.shape[1], LL.shape[0]))

    # Normalize watermark to keep changes minimal
    normalized_watermark = resized_watermark / 255.0

    # Embed the watermark in the LL subband
    watermarked_LL = LL + normalized_watermark

    # Reconstruct the watermarked Y channel
    watermarked_coeffs = (watermarked_LL, (LH, HL, HH))
    watermarked_y_channel = pywt.idwt2(watermarked_coeffs, 'haar')

    # Clip values to be in valid pixel range (0-255)
    watermarked_y_channel = np.clip(watermarked_y_channel, 0, 255).astype(np.uint8)

    # Update the Y channel in the YUV image
    yuv_image[:, :, 0] = watermarked_y_channel

    # Convert the watermarked image back to BGR color space
    watermarked_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    return watermarked_image


def save_image(image: np.ndarray, output_path: str) -> None:
    cv2.imwrite(output_path, image)


def main():
    # Load the input image
    image_path = "./test_image.png"
    image = load_image(image_path)

    # Create a star shape watermark
    watermark = create_star_shape_watermark(128)

    # Embed the watermark using DWT
    watermarked_image = embed_watermark_dwt(image, watermark)

    # Save the watermarked image
    output_path = "./watermarked_image.png"
    save_image(watermarked_image, output_path)


def test():
    assert os.path.exists("./watermarked_image.png") == True

    result = cv2.imread("./watermarked_image.png")
    
    input_image = cv2.imread("./test_image.png")
    watermark = create_star_shape_watermark(128)
    watermarked_image = embed_watermark_dwt(input_image, watermark)

    assert np.allclose(result, watermarked_image)

    # Clean up
    # os.remove("./watermarked_image.png")


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")
