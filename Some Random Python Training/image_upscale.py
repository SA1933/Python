import cv2
from realesrgan import RealESRGAN
import os

def upscale_image(input_path, output_path):
    """
    Upscale an image to 4K resolution using Real-ESRGAN.

    :param input_path: Path to the input image
    :param output_path: Path to save the upscaled image
    """
    # Load Real-ESRGAN model
    model = RealESRGAN('weights/RealESRGAN_x4plus.pth', scale=4)

    # Read input image
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Failed to load the image. Check the input path.")

    # Upscale the image
    upscaled_image = model.predict(image)

    # Save the upscaled image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, upscaled_image)
    print(f"Upscaled image saved to: {output_path}")

if __name__ == "__main__":
    input_image = "path_to_input_image.jpg"  # Replace with your input image path
    output_image = "path_to_output_directory/upscaled_image.png"  # Replace with your desired output path
    
    try:
        upscale_image(input_image, output_image)
    except Exception as e:
        print(f"Error: {e}")