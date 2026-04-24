# Image Compressor

A Python script that compresses images and converts them to WebP format using [Pillow](https://pillow.readthedocs.io/).

## Supported Formats

JPG, JPEG, PNG, WebP, TIFF, BMP

## How to Run

```bash
# Step 1: Install Python (3.8+)

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the compression script
python compress.py
```

## What It Does

1. Creates `raw/` and `compressed/` directories if they don't exist
2. Reads all images from the `raw/` folder
3. Resizes images larger than 1920px (preserving aspect ratio)
4. Compresses and converts them to WebP at 60% quality
5. Saves compressed images to the `compressed/` folder
6. Logs the original size, compressed size, and percentage saved for each image

## Usage

1. Place your images inside the `raw/` folder
2. Run: `python compress.py`
3. Your compressed images will appear in the `compressed/` folder

## Build as EXE (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --name image-compressor compress.py
```

The executable will be in the `dist/` folder.
