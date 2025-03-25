from Image_Segmentation_Using_Kmeans import segment_image_using_kmeans

def test_Image_Segmentation_Using_Kmeans(image_path: str, k: int, output_path: str) -> None:
    """
    Test the functionality of the Image_Segmentation_Using_Kmeans module.

    Args:
        image_path (str): The file path of the input image.
        k (int): The number of clusters to use for K-means clustering.
        output_path (str): The file path where the segmented image will be saved.

    Raises:
        AssertionError: If any of the module's functions do not work as expected.
    """
    try:
        # Test the wrapper function
        segment_image_using_kmeans(image_path, k, output_path)
        print(f"Segmentation completed successfully. Output saved to '{output_path}'.")
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise AssertionError(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Segmentation_Using_Kmeans("./seg_image.png", 4, "./seg_image_kmeans.png")