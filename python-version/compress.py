import os
import sys
from PIL import Image

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".bmp"}

def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def compress_image(file_path, output_path, quality=60):
    img = Image.open(file_path)
    img.save(output_path, optimize=True, quality=quality)

    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(output_path)
    saved = ((original_size - compressed_size) / original_size) * 100

    name = os.path.basename(file_path)
    print(f"{name}: {original_size / 1024:.1f}KB -> {compressed_size / 1024:.1f}KB ({saved:.1f}% saved)")

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
            os.path.join(compressed_dir, file),
        )

    print("\nDone! Compressed images are in the compressed/ folder.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
