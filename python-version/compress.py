import os
import sys
from PIL import Image

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".bmp"}
MAX_DIMENSION = 1920

def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def compress_image(file_path, output_dir, quality=60):
    img = Image.open(file_path)
    name = os.path.basename(file_path)
    output_name = os.path.splitext(name)[0] + ".webp"
    output_path = os.path.join(output_dir, output_name)

    original_width, original_height = img.size
    img.thumbnail((MAX_DIMENSION, MAX_DIMENSION))
    new_width, new_height = img.size

    img.save(output_path, format="WEBP", quality=quality)

    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(output_path)
    saved = ((original_size - compressed_size) / original_size) * 100

    resized = f" | resized {original_width}x{original_height} -> {new_width}x{new_height}" if (original_width, original_height) != (new_width, new_height) else ""
    print(f"{name} -> {output_name}: {original_size / 1024:.1f}KB -> {compressed_size / 1024:.1f}KB ({saved:.1f}% saved){resized}")

def main():
    base = get_base_dir()
    raw_dir = os.path.join(base, "raw")
    compressed_dir = os.path.join(base, "compressed")

    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(compressed_dir, exist_ok=True)

    files = [
        f for f in os.listdir(raw_dir)
        if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        print("No images found in raw/ folder. Add images there and run again.")
        input("Press Enter to exit...")
        return

    print(f"Compressing {len(files)} image(s)...\n")

    for file in files:
        compress_image(
            os.path.join(raw_dir, file),
            compressed_dir,
        )

    print("\nDone! Compressed images are in the compressed/ folder.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
