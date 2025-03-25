from extract_and_save_features import extract_and_save_features

def feature_extraction_module(image_path: str) -> None:
    """
    Extracts and saves HOG and LBP features from the given image. Handles both 3-channel (RGB) and 4-channel (RGBA) images.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").

    Returns:
        None: The function saves the extracted features directly to files:
            - HOG features are saved as "hog_features.npy".
            - LBP features are saved as "lbp_features.npy".

    Example:
        feature_extraction_module("./test_image.png")
    """
    extract_and_save_features(image_path)