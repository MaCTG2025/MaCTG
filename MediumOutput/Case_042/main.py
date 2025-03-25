from Feature_Extraction_Module import feature_extraction_module

def main() -> None:
    """
    Entry point for the feature extraction project. Calls the feature extraction module to process the image.

    Args:
        None

    Returns:
        None: The function triggers the feature extraction process and saves the results to files.
    """
    feature_extraction_module("./test_image.png")

if __name__ == '__main__':
    main()