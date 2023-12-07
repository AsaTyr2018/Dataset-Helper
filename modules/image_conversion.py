import tkinter as tk
from tkinter import ttk
import os
import random
from PIL import Image
import subprocess

def convert_and_rename_images(folder_path):
    image_formats = [".webp", ".jpg", ".jpeg", ".bmp", ".tiff", ".png"]
    avif_format = ".avif"
    temp_suffix = "_temp_rename_"

    # Reset image counter
    image_counter = 0

    # First pass: Rename to temporary file names
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if any(filename.endswith(format) for format in image_formats) or filename.endswith(avif_format):
                try:
                    temp_name = f"{temp_suffix}{random.randint(1000, 9999)}.png"
                    temp_path = os.path.join(root, temp_name)
                    original_path = os.path.join(root, filename)
                    os.rename(original_path, temp_path)
                except PermissionError:
                    print(f"Skipping locked file: {filename}")

    # Second pass: Convert and finally rename
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.startswith(temp_suffix):
                process_image(root, filename, image_counter, image_formats, avif_format)
                image_counter += 1

def process_image(root, filename, counter, image_formats, avif_format):
    temp_path = os.path.join(root, filename)

    # Convert to PNG
    if any(filename.endswith(format) for format in image_formats):
        with Image.open(temp_path) as img:
            img.save(temp_path, "PNG")
    elif filename.endswith(avif_format):
        subprocess.run(["ffmpeg", "-i", temp_path, temp_path])

    # Rename the converted image
    rename_image(temp_path, root, counter)

def rename_image(image_path, root_folder, counter):
    project_name = os.path.basename(root_folder)
    new_name = f"{project_name}{counter:02}.png"
    new_path = os.path.join(root_folder, new_name)
    os.rename(image_path, new_path)

def create_image_conversion_tab(notebook):
    image_conversion_frame = ttk.Frame(notebook)
    notebook.add(image_conversion_frame, text="Image Conversion")

    image_folder_label = tk.Label(image_conversion_frame, text="Folder Path:")
    image_folder_label.pack()
    image_folder_entry = tk.Entry(image_conversion_frame, width=50)
    image_folder_entry.pack()

    convert_and_rename_button = tk.Button(image_conversion_frame, text="Convert and Rename Images")
    convert_and_rename_button.pack()

    def convert_and_rename_button_click():
        folder_path = image_folder_entry.get()
        convert_and_rename_images(folder_path)

    convert_and_rename_button.config(command=convert_and_rename_button_click)

if __name__ == "__main__":
    root = tk.Tk()
    notebook = ttk.Notebook(root)
    notebook.pack()
    create_image_conversion_tab(notebook)
    root.mainloop()
