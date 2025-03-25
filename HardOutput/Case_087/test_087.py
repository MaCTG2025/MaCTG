'''
Given an input image ("./texture_icon.jpg"), apply texture systhesizing using Efros_Leung algorithm to expand the image to 128x128 pixels. Save the result as "texture_synthesized.png". Set np.random.seed to 0 before starting the algorithm.
'''

import cv2
import numpy as np
from pathlib import Path
import os

def load_image(image_path: Path) -> np.ndarray:
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Cannot load image at '{image_path}'")
    return image

def initialize_synthesized_image(input_texture: np.ndarray, output_size: tuple, seed_size: int) -> np.ndarray:
    h, w, c = input_texture.shape
    H, W = output_size

    synthesized = -np.ones((H, W, c), dtype=np.int16)

    max_y = h - seed_size
    max_x = w - seed_size
    seed_y = np.random.randint(0, max_y + 1)
    seed_x = np.random.randint(0, max_x + 1)
    seed_patch = input_texture[seed_y:seed_y + seed_size, seed_x:seed_x + seed_size]

    start_y = (H - seed_size) // 2
    start_x = (W - seed_size) // 2
    synthesized[start_y:start_y + seed_size, start_x:start_x + seed_size] = seed_patch

    return synthesized

def get_boundary_pixels(synthesized: np.ndarray) -> list:
    H, W, _ = synthesized.shape
    known_mask = synthesized[:, :, 0] != -1
    unknown_mask = ~known_mask

    kernel = np.ones((3, 3), dtype=np.uint8)
    dilated_known = cv2.dilate(known_mask.astype(np.uint8), kernel, iterations=1)
    boundary_mask = dilated_known.astype(bool) & unknown_mask

    boundary_pixels = np.argwhere(boundary_mask)
    return boundary_pixels.tolist()

def texture_synthesize(input_texture: np.ndarray, output_size: tuple) -> np.ndarray:
    h, w, c = input_texture.shape
    H, W = output_size

    seed_size = 5  # Adjusted seed size
    synthesized = initialize_synthesized_image(input_texture, output_size, seed_size)

    WINDOW_SIZE = 7  # Adjusted window size
    HALF_WINDOW = WINDOW_SIZE // 2
    ERROR_TOLERANCE = 0.3  # Adjusted error tolerance

    total_pixels = H * W
    unknown_pixels = np.sum(synthesized[:, :, 0] == -1)
    progress = True

    while unknown_pixels > 0 and progress:
        progress = False
        boundary_pixels = get_boundary_pixels(synthesized)

        print(f"Unknown pixels remaining: {unknown_pixels}, Boundary pixels: {len(boundary_pixels)}")

        for y, x in boundary_pixels:
            y_min = y - HALF_WINDOW
            y_max = y + HALF_WINDOW + 1
            x_min = x - HALF_WINDOW
            x_max = x + HALF_WINDOW + 1

            synthesized_window = np.zeros((WINDOW_SIZE, WINDOW_SIZE, c), dtype=np.int16) - 1

            sy_min = max(0, -y_min)
            sy_max = WINDOW_SIZE - max(0, y_max - H)
            sx_min = max(0, -x_min)
            sx_max = WINDOW_SIZE - max(0, x_max - W)

            wy_min = max(y_min, 0)
            wy_max = min(y_max, H)
            wx_min = max(x_min, 0)
            wx_max = min(x_max, W)

            synthesized_window[sy_min:sy_max, sx_min:sx_max] = synthesized[wy_min:wy_max, wx_min:wx_max]

            known_mask = synthesized_window[:, :, 0] != -1

            if np.sum(known_mask) == 0:
                continue

            template = synthesized_window.copy()

            # Limit the search to random samples to speed up
            sample_size = 1000  # Adjust as needed
            ty_choices = np.random.randint(HALF_WINDOW, h - HALF_WINDOW, size=sample_size)
            tx_choices = np.random.randint(HALF_WINDOW, w - HALF_WINDOW, size=sample_size)

            min_error = None
            candidate_pixels = []

            for ty, tx in zip(ty_choices, tx_choices):
                input_window = input_texture[ty - HALF_WINDOW:ty + HALF_WINDOW + 1,
                                             tx - HALF_WINDOW:tx + HALF_WINDOW + 1]

                input_known = input_window[known_mask]
                template_known = template[known_mask]

                ssd = np.sum((input_known.astype(np.int32) - template_known.astype(np.int32)) ** 2)

                if min_error is None or ssd < min_error:
                    min_error = ssd
                    candidate_pixels = [input_texture[ty, tx]]
                elif ssd <= min_error * (1 + ERROR_TOLERANCE):
                    candidate_pixels.append(input_texture[ty, tx])

            if candidate_pixels:
                selected_pixel = candidate_pixels[np.random.randint(len(candidate_pixels))]
                synthesized[y, x] = selected_pixel
                progress = True
                unknown_pixels -= 1

        if not progress:
            unknown_indices = np.where(synthesized[:, :, 0] == -1)
            for y, x in zip(unknown_indices[0], unknown_indices[1]):
                ry = np.random.randint(0, h)
                rx = np.random.randint(0, w)
                synthesized[y, x] = input_texture[ry, rx]
            break

    synthesized = synthesized.astype(np.uint8)
    return synthesized

def save_image(image: np.ndarray, output_path: Path):
    cv2.imwrite(str(output_path), image)
    print(f"Synthesized texture saved to '{output_path}'")

def main():
    np.random.seed(0)

    image_path = Path('./texture_icon.jpg')
    output_path = Path('texture_synthesized.png')

    input_texture = load_image(image_path)
    output_size = (128, 128)  # Adjusted for testing

    synthesized = texture_synthesize(input_texture, output_size)
    save_image(synthesized, output_path)

def test():
    np.random.seed(0)

    image_path = Path('./texture_icon.jpg')
    output_path = Path('texture_synthesized.png')

    input_texture = load_image(image_path)
    output_size = (128, 128)

    synthesized = texture_synthesize(input_texture, output_size)
    result = load_image(output_path)

    assert np.allclose(synthesized, result)

    # clean up
    # os.remove(output_path)


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")
