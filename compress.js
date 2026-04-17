const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const RAW_DIR = path.join(__dirname, "raw");
const COMPRESSED_DIR = path.join(__dirname, "compressed");

const SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".avif"];

// Ensure directories exist
if (!fs.existsSync(RAW_DIR)) fs.mkdirSync(RAW_DIR);
if (!fs.existsSync(COMPRESSED_DIR)) fs.mkdirSync(COMPRESSED_DIR);

async function compressImage(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const fileName = path.basename(filePath);
  const outputPath = path.join(COMPRESSED_DIR, fileName);

  let pipeline = sharp(filePath);
  const quality = 60;
  if (ext === ".png") {
    pipeline = pipeline.png({ quality });
  } else if (ext === ".jpg" || ext === ".jpeg") {
    pipeline = pipeline.jpeg({ quality });
  } else if (ext === ".webp") {
    pipeline = pipeline.webp({ quality });
  } else if (ext === ".tiff") {
    pipeline = pipeline.tiff({ quality });
  } else if (ext === ".avif") {
    pipeline = pipeline.avif({ quality });
  }

  await pipeline.toFile(outputPath);

  const originalSize = fs.statSync(filePath).size;
  const compressedSize = fs.statSync(outputPath).size;
  const saved = (((originalSize - compressedSize) / originalSize) * 100).toFixed(1);

  console.log(`${fileName}: ${(originalSize / 1024).toFixed(1)}KB -> ${(compressedSize / 1024).toFixed(1)}KB (${saved}% saved)`);
}

async function main() {
  const files = fs.readdirSync(RAW_DIR).filter((f) => {
    return SUPPORTED_EXTENSIONS.includes(path.extname(f).toLowerCase());
  });

  if (files.length === 0) {
    console.log("No images found in raw/ directory. Add images there and run again.");
    return;
  }

  console.log(`Compressing ${files.length} image(s)...\n`);

  for (const file of files) {
    await compressImage(path.join(RAW_DIR, file));
  }

  console.log("\nDone! Compressed images are in the compressed/ directory.");
}

main().catch(console.error);
