# Batch Image Resizer CLI

A lightweight, high-performance Python command-line utility for batch resizing images in a directory with automated format conversion and error handling.

## Features

- **Batch Processing:** Automatically scans and resizes all image assets (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`) within a target directory.
- **Format Conversion:** Convert images on-the-fly to a specified target format (e.g., JPEG, PNG, WEBP).
- **Automated Fallback Handling:** Automatically converts `RGBA` transparent color spaces to `RGB` if saving into formats that do not support transparency (such as JPEG).
- **Directory Safety Checks:** Verifies destination directories and prompts before overwriting existing folders to prevent data loss.
- **High Quality Resampling:** Utilizes Pillow's `LANCZOS` resampling filter for optimal downscaling quality.

## Requirements

- Python 3.6+
- Pillow (`PIL`)

Install dependencies via `pip`:

```bash
pip install Pillow
```

# Arguments 
| Flag | Long Flag | Description | Required | Default |
| :--- | :--- | :--- | :---: | :---: |
| `-i` | `--input_dir` | Path to the directory containing input images. | **Yes** | — |
| `-o` | `--output_dir` | Path to save the resized output images. | **Yes** | — |
| `-w` | `--width` | Target width in pixels. | **Yes** | — |
| `-H` | `--height` | Target height in pixels. | **Yes** | — |
| `-f` | `--format` | Output image format (e.g., JPEG, PNG, WEBP). | No | `JPEG` |

# Usage
```bash
python resizer.py -i ./raw_icons -o ./resized_icons -w 32 -H 32 -f PNG
```
