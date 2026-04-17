# Image Compressor

A Node.js script that compresses images using [sharp](https://sharp.pixelplumbing.com/).

## Supported Formats

JPG, JPEG, PNG, WebP, TIFF, AVIF

## How to Run

```bash
# Step 1: Install Node.js (any LTS version) — run in PowerShell as Administrator
winget install OpenJS.NodeJS.LTS

# Step 2: Install dependencies
npm install

# Step 3: Run the compression script
npm run compress
```

## What It Does

1. Creates `raw/` and `compressed/` directories if they don't exist
2. Reads all images from the `raw/` folder
3. Compresses them at 60% quality using sharp
4. Saves compressed images to the `compressed/` folder
5. Logs the original size, compressed size, and percentage saved for each image

## For the User

1. Place your images inside the `raw/` folder
2. Ask Codex to run: `npm install && npm run compress`
3. Your compressed images will appear in the `compressed/` folder
