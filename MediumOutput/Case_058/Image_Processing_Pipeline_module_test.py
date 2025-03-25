from Image_Processing_Pipeline import image_processing_pipeline

def test_Image_Processing_Pipeline() -> None:
    """
    Tests the basic functionality of the Image_Processing_Pipeline module.
    """
    # Test with default parameters
    image_processing_pipeline("./test_image.png", output_path="test_image_edges_default.png")
    
    # Test with custom parameters (optional, if supported by the module)
    # image_processing_pipeline("./test_image.png", output_path="test_image_edges_custom.png")

if __name__ == '__main__':
    test_Image_Processing_Pipeline()