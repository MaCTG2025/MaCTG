'''
Given an input image ("./test_image.png"), develop an algorithm to resize it into 1.2x width by inserting seams based on energy functions, without distorting important content, save the output image as "./test_image_double_size.png".
'''


import cv2
import numpy as np
import os
from typing import Tuple


def load_image(image_path: str) -> np.ndarray:
    return cv2.imread(image_path)

def compute_energy(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    return np.abs(sobelx) + np.abs(sobely)

def find_vertical_seam(energy: np.ndarray, k: int = 1) -> list:
    h, w = energy.shape
    energy_map = energy.copy()
    seams = []

    for _ in range(k):
        M = energy_map.copy()
        backtrack = np.zeros_like(M, dtype=int)
        
        # Compute cumulative energy map
        for i in range(1, h):
            for j in range(w):
                if j == 0:
                    idx = np.argmin(M[i - 1, j:j + 2])
                    offset = idx + j
                elif j == w - 1:
                    idx = np.argmin(M[i - 1, j - 1:j + 1])
                    offset = idx + j - 1
                else:
                    idx = np.argmin(M[i - 1, j - 1:j + 2])
                    offset = idx + j - 1
                M[i, j] += M[i - 1, offset]
                backtrack[i, j] = offset

        # Find the minimal energy seam
        seam = []
        j = np.argmin(M[-1])
        for i in reversed(range(h)):
            seam.append((i, j))
            # Mark the seam pixel with infinity to prevent reuse
            energy_map[i, j] = np.inf
            j = backtrack[i, j]
        seam.reverse()
        seams.append(seam)
    return seams


def duplicate_seam(img: np.ndarray, seams: list) -> np.ndarray:
    h, w, c = img.shape
    seams = sorted(seams, key=lambda x: [p[1] for p in x])
    output = np.zeros((h, w + len(seams), c), dtype=img.dtype)

    # Create a map to record where seams are to be added
    seam_map = np.zeros((h, w), dtype=bool)
    for seam in seams:
        for i, j in seam:
            seam_map[i, j] = True

    for i in range(h):
        k = 0  # Offset for the new image width
        for j in range(w):
            output[i, j + k] = img[i, j]
            if seam_map[i, j]:
                # Duplicate the pixel
                output[i, j + k + 1] = img[i, j]
                k += 1
    return output

def enlarge_width(img: np.ndarray, scale: float) -> np.ndarray:
    new_width = int(img.shape[1] * scale)
    delta = new_width - img.shape[1]
    img_output = img.copy()

    energy = compute_energy(img_output)
    seams = find_vertical_seam(energy, delta)
    img_output = duplicate_seam(img_output, seams)
    return img_output

def main():
    image_path = "./test_image.png"
    output_path = "./test_image_double_size.png"
    scale = 1.2
    img = load_image(image_path)
    img_output = enlarge_width(img, scale)
    cv2.imwrite(output_path, img_output)

def test():
    image_path = "./test_image.png"
    img = load_image(image_path)
    img_output = enlarge_width(img, 1.2)
    
    result = cv2.imread("./test_image_double_size.png")

    assert np.allclose(img_output, result)

    # clean up
    # os.remove("./test_image_double_size.png")

if __name__ == "__main__":
    # main()
    test()
    print("All tests passed")