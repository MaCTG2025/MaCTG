from Blob_Detection_and_Analysis import blob_detection_and_analysis_module

def main() -> None:
    """
    Entry point for the blob detection and analysis project.
    Detects blobs in the given image, computes their center, area, and perimeter,
    and saves the results into a .npy file.

    Example:
    --------
    main()
    """
    blob_detection_and_analysis_module("./blobs.jpg", "blobs.npy")

if __name__ == '__main__':
    main()