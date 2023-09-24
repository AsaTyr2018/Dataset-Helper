import tkinter as tk
from tkinter import ttk
import os
from PIL import Image
import subprocess

def convert_images(folder_path):
    image_formats = [".webp", ".jpg", ".jpeg", ".bmp", ".tiff"]
    avif_format = ".avif"
    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            original_path = os.path.join(root, filename)
            png_path = os.path.splitext(original_path)[0] + ".png"
            
            if any(filename.endswith(format) for format in image_formats):
                with Image.open(original_path) as img:
                    img.save(png_path, "PNG")
                os.remove(original_path)
            elif filename.endswith(avif_format):
                subprocess.run(["ffmpeg", "-i", original_path, png_path])
                os.remove(original_path)

def create_image_conversion_tab(notebook):
    image_conversion_frame = ttk.Frame(notebook)
    notebook.add(image_conversion_frame, text="Image Conversion")

    image_folder_label = tk.Label(image_conversion_frame, text="Folder Path:")
    image_folder_label.pack()
    image_folder_entry = tk.Entry(image_conversion_frame, width=50)
    image_folder_entry.pack()

    convert_images_button = tk.Button(image_conversion_frame, text="Convert Images to PNG")
    convert_images_button.pack()

    def convert_images_button_click():
        folder_path = image_folder_entry.get()
        convert_images(folder_path)

    convert_images_button.config(command=convert_images_button_click)
