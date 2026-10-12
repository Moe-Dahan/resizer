#!/usr/bin/env python3

import argparse
import PIL.Image as Image
import os

def check_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False

def resize_image(input_path, output_path, width, height, image_format):
    for images in os.listdir(input_path):
        if images.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(os.path.join(input_path, images)) as img:
                img = img.resize((width, height), Image.LANCZOS)
                try:
                    img.save(os.path.join(output_path, images.replace(images.split('.')[-1], image_format.lower())), format=image_format)
                except Exception as e:
                    rgb_im = img.convert('RGB')
                    rgb_im.save(os.path.join(output_path, images.replace(images.split('.')[-1], image_format.lower())), format=image_format)
                print(f"Resized image: {images} to {width}x{height} and saving as {image_format} format. saved in {output_path}")

def parse_args():
    parser = argparse.ArgumentParser(description="Resize images in a directory.")
    parser.add_argument('-i', '--input_dir', required=True, type=str, help="Path to the input directory containing images.")
    parser.add_argument('-o', '--output_dir', required=True, type=str, help="Path to the output directory to save resized images.")
    parser.add_argument('-w', '--width', required=True, type=int, help="The target width for resizing.")
    parser.add_argument('-H', '--height', required=True, type=int, help="The target height for resizing.")
    parser.add_argument('-f', '--format', required=False, type=str, default='JPEG', help="The format to save resized images (default: JPEG).")
    args = parser.parse_args()
    if check_directory(args.output_dir):
        resize_image(args.input_dir, args.output_dir, args.width, args.height, args.format)
    else:
        print(f"Output directory '{args.output_dir}' already exists. Please choose a different directory or remove the existing one.")
        overwrite = input("Do you want to overwrite the existing directory? (y/n): ").strip().lower()
        if overwrite == 'y':
            resize_image(args.input_dir, args.output_dir, args.width, args.height, args.format)
        else:
            print("Operation cancelled!")


if __name__ == "__main__":
    parse_args()