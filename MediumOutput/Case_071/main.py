from load_images import load_images
from transform_object_image import transform_object_image
from seamless_cloning import seamless_cloning
from save_image import save_image

def image_transformation_and_seamless_cloning(background_path: str, object_path: str, output_path: str) -> None:
    """
    Orchestrate the entire process of loading, transforming, blending, and saving images.

    Args:
        background_path (str): The file path to the background image.
        object_path (str): The file path to the object image.
        output_path (str): The file path where the final blended image will be saved.

    Returns:
        None

    This function sequentially loads the background and object images, transforms the object image,
    blends it onto the background using seamless cloning, and saves the final result.
    """

    # Load images
    background, object_img = load_images(background_path, object_path)

    # Transform object image
    transformed_object = transform_object_image(object_img)

    # Perform seamless cloning
    blended_image = seamless_cloning(background, transformed_object)

    # Save the final blended image
    save_image(blended_image, output_path)


if __name__ == '__main__':
    image_transformation_and_seamless_cloning('./abraham.jpg', './test_image.png', 'seamless_cloning.png')