import os
from pathlib import Path
from blur import ImageBlur  # Assuming your class is saved as blur.py

# Define input and output directories
INPUT_DIR = 'images'
OUTPUT_DIR = 'images/blurred'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Supported image extensions
SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')

def process_images():
    # Initialize ImageBlur instance
    blur_tool = ImageBlur('./model/best.pt')

    # List all image files in input directory
    image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(SUPPORTED_EXTENSIONS)]

    if not image_files:
        print(f"No supported image files found in '{INPUT_DIR}'.")
        return

    print(f"Found {len(image_files)} image(s) to process.")

    # Process each image
    for image_file in image_files:
        input_path = os.path.join(INPUT_DIR, image_file)
        output_path = os.path.join(OUTPUT_DIR, image_file)

        try:
            print(f"Processing '{image_file}'...")
            plates_count = blur_tool.blurLicencePlate(input_path, output_path)
            print(f"--> {plates_count} license plate(s) blurred. Saved to '{output_path}'.")
        except Exception as e:
            print(f"Error processing '{image_file}': {e}")

if __name__ == "__main__":
    process_images()
