'''
Given an input image ("./Phantom.png"), apply Radon transform to the image and save the output image as "Radon_transformed_Phantom.png". Then apply inverse Radon transform to the transformed image and save the output image as "Inverse_Radon_transformed_Phantom.png".
'''


import cv2
import numpy as np
import os


def load_image(image_path: str) -> np.ndarray:
    # Load the input image as grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: could not load image from {image_path}")
        exit(1)
    return image

def radon_transform(image: np.ndarray, angles: np.ndarray) -> np.ndarray:
    """
    Perform the Radon transform by rotating the image at different angles and 
    summing the pixel values along the vertical axis to get projections.
    """
    # Create an empty sinogram (projection matrix)
    sinogram = np.zeros((image.shape[0], len(angles)))

    # Perform the Radon transform by rotating and summing the projections
    for i, angle in enumerate(angles):
        # Rotate the image by the given angle (without reshaping, preserving dimensions)
        rotated_image = rotate_image(image, angle)
        # Sum the pixel values along the vertical axis (axis=0)
        sinogram[:, i] = np.sum(rotated_image, axis=0)

    return sinogram

def rotate_image(image: np.ndarray, angle: float) -> np.ndarray:
    """
    Rotate the image by the given angle around its center using OpenCV.
    """
    (h, w) = image.shape
    # Calculate the center of the image
    center = (w // 2, h // 2)
    # Get the rotation matrix for the given angle
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Rotate the image
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return rotated

def ramp_filter(projection: np.ndarray) -> np.ndarray:
    """
    Apply a simple ramp filter in the frequency domain to the projection.
    This will help improve the sharpness of the reconstruction.
    """
    # Perform the Fourier Transform of the projection
    projection_fft = np.fft.fft(projection)

    # Create a ramp filter in the frequency domain
    frequencies = np.fft.fftfreq(len(projection))
    ramp = np.abs(frequencies)  # Ramp function (high-pass filter)

    # Apply the ramp filter
    filtered_fft = projection_fft * ramp

    # Perform the inverse Fourier transform to get the filtered projection
    filtered_projection = np.real(np.fft.ifft(filtered_fft))

    return filtered_projection

def inverse_radon_transform(sinogram: np.ndarray, angles: np.ndarray) -> np.ndarray:
    """
    Perform inverse Radon transform using filtered back-projection.
    Apply ramp filtering to each projection to improve reconstruction quality.
    """
    # Initialize the reconstructed image
    reconstructed_image = np.zeros((sinogram.shape[0], sinogram.shape[0]))

    # Perform back-projection
    for i, angle in enumerate(angles):
        # Apply ramp filter to the current projection
        filtered_projection = ramp_filter(sinogram[:, i])
        
        # Create a 2D image of the filtered projection by repeating it across the image height
        projection = np.tile(filtered_projection, (sinogram.shape[0], 1))
        
        # Rotate the projection back by the negative of the angle
        back_projected = rotate_image(projection, -angle)
        
        # Accumulate the back-projected image
        reconstructed_image += back_projected

    # Normalize the reconstructed image
    reconstructed_image = reconstructed_image / len(angles)

    return reconstructed_image

def save_image(image: np.ndarray, output_path: str) -> None:
    # Save the image (normalize to [0, 255] and convert to uint8)
    normalized_image = (image - np.min(image)) / (np.max(image) - np.min(image)) * 255
    cv2.imwrite(output_path, normalized_image.astype(np.uint8))

def main():
    # Load the input image
    image_path = "Phantom.png"
    image = load_image(image_path)

    # Define the angles for the Radon transform (from 0 to 180 degrees)
    angles = np.linspace(0., 180., max(image.shape), endpoint=False)

    # Apply the Radon transform
    radon_image = radon_transform(image, angles)
    
    # Save the Radon transformed image
    save_image(radon_image, "Radon_transformed_Phantom.png")

    # Apply the inverse Radon transform (filtered back-projection)
    reconstructed_image = inverse_radon_transform(radon_image, angles)

    # Save the reconstructed (inverse Radon) image
    save_image(reconstructed_image, "Inverse_Radon_transformed_Phantom.png")


def test():
    assert os.path.exists("Radon_transformed_Phantom.png") == True
    assert os.path.exists("Inverse_Radon_transformed_Phantom.png") == True

    radon_transformed = cv2.imread("Radon_transformed_Phantom.png", cv2.IMREAD_GRAYSCALE)
    inverse_radon_transformed = cv2.imread("Inverse_Radon_transformed_Phantom.png", cv2.IMREAD_GRAYSCALE)

    input_image = cv2.imread("Phantom.png", cv2.IMREAD_GRAYSCALE)
    angles = np.linspace(0., 180., max(input_image.shape), endpoint=False)
    radon_image = radon_transform(input_image, angles)
    iradon_image = inverse_radon_transform(radon_image, angles)

    radon_image = (radon_image - np.min(radon_image)) / (np.max(radon_image) - np.min(radon_image)) * 255
    iradon_image = (iradon_image - np.min(iradon_image)) / (np.max(iradon_image) - np.min(iradon_image)) * 255
    assert np.allclose(radon_transformed, radon_image.astype(np.uint8))
    assert np.allclose(inverse_radon_transformed, iradon_image.astype(np.uint8))

    # Clean up
    # os.remove("Radon_transformed_Phantom.png")
    # os.remove("Inverse_Radon_transformed_Phantom.png")


if __name__ == "__main__":
    # main()
    test()
    print("All tests passed.")