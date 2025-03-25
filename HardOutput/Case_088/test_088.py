'''
Given an input image ("./test_image.png"), add oil painting effect to the image and save the output image as "./output_image.png".
'''


import cv2
import numpy as np
import os


def load_image(image_path: str) -> np.ndarray:
    image = cv2.imread(image_path)
    return image

def oil_painting_effect(img, radius=5, intensity_levels=8):
    # Get the image dimensions
    height, width, _ = img.shape

    # Create the output image
    output = np.zeros_like(img)

    # Set intensity range (for each channel)
    intensity_range = 256 // intensity_levels

    for y in range(radius, height - radius):
        for x in range(radius, width - radius):
            # Define the neighborhood
            neighborhood = img[y - radius:y + radius + 1, x - radius:x + radius + 1]

            # Create histograms for each color channel (B, G, R)
            hist_b = cv2.calcHist([neighborhood], [0], None, [intensity_levels], [0, 256])
            hist_g = cv2.calcHist([neighborhood], [1], None, [intensity_levels], [0, 256])
            hist_r = cv2.calcHist([neighborhood], [2], None, [intensity_levels], [0, 256])

            # Find the most common intensity for each channel
            most_common_b = np.argmax(hist_b)
            most_common_g = np.argmax(hist_g)
            most_common_r = np.argmax(hist_r)

            # Mask pixels in the neighborhood that have the most common intensities
            mask_b = (neighborhood[:, :, 0] >= most_common_b * intensity_range) & (neighborhood[:, :, 0] < (most_common_b + 1) * intensity_range)
            mask_g = (neighborhood[:, :, 1] >= most_common_g * intensity_range) & (neighborhood[:, :, 1] < (most_common_g + 1) * intensity_range)
            mask_r = (neighborhood[:, :, 2] >= most_common_r * intensity_range) & (neighborhood[:, :, 2] < (most_common_r + 1) * intensity_range)

            # Combine the masks for B, G, and R channels
            combined_mask = mask_b & mask_g & mask_r

            # Calculate the mean color of the pixels in the neighborhood that match the combined mask
            if np.any(combined_mask):
                mean_color = cv2.mean(neighborhood, combined_mask.astype(np.uint8))

                # Set the output pixel to the calculated mean color
                output[y, x] = mean_color[:3]

    return output

def save_image(image: np.ndarray, output_path: str) -> None:
    cv2.imwrite(output_path, image)

def main():
    image_path = "./test_image.png"
    output_path = "./output_image.png"
    radius = 3
    levels = 5
    image = load_image(image_path)
    output = oil_painting_effect(image, radius, levels)
    save_image(output, output_path)

def test():
    assert os.path.exists("./output_image.png") == True

    result = cv2.imread("./output_image.png")

    input_image = cv2.imread("./test_image.png")
    r = 3
    levels = 5
    output_image = oil_painting_effect(input_image, r, levels)

    assert np.allclose(result, output_image)

    # clean up
    # os.remove("./output_image.png")


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")