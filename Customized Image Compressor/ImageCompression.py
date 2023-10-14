import cv2
import numpy as np
from PIL import Image
import os

def compress_image(input_image_path, output_image_path, target_size_kb):
    # Initialize the quality parameter for JPEG compression
    quality = 90

    while os.path.getsize(output_image_path) / 1024 > target_size_kb:
        # Load the image
        image = cv2.imread(input_image_path)

        # Compress the image using JPEG with the specified quality
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        _, buffer = cv2.imencode(".jpg", image, encode_param)

        # Convert the buffer to an image using PIL
        image = Image.fromarray(np.uint8(buffer))

        # Save the image to the output path
        image.save(output_image_path , "JPEG")

        # Reduce the quality for the next iteration
        quality -= 10

if __name__ == "__main__":
    input_image_path = "a.PNG"
    output_image_path = "a.PNG"

    # Specify the target file size in KB
    target_size_kb = float(input("Enter the target file size in KB: "))

    # Perform image compression
    compress_image(input_image_path,output_image_path , target_size_kb)

    print(f"Image has been compressed and saved as '{output_image_path}'")
