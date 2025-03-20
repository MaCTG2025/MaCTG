from Image_Arithmetic_Operations import image_arithmetic_module

def test_image_arithmetic_module(image_path: str, value: int) -> None:
    """
    Tests the functionality of the `image_arithmetic_module` function.

    This function verifies that the module correctly applies arithmetic addition and subtraction
    operations to the input image and returns the paths to the resulting images.

    Args:
        image_path (str): The file path to the input image.
        value (int): The integer value to use for the arithmetic operations.
    """
    # Call the module function
    added_image_path, subtracted_image_path = image_arithmetic_module(image_path, value)

    # Verify the output types
    assert isinstance(added_image_path, str), "added_image_path should be a string."
    assert isinstance(subtracted_image_path, str), "subtracted_image_path should be a string."

    # Verify that the output files exist
    import os
    assert os.path.exists(added_image_path), f"File {added_image_path} does not exist."
    assert os.path.exists(subtracted_image_path), f"File {subtracted_image_path} does not exist."

    print("Test passed: Output files created successfully.")

if __name__ == '__main__':
    test_image_arithmetic_module("./test_image.png", 100)