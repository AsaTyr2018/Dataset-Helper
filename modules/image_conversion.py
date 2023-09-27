import tkinter as tk
from tkinter import ttk
import os
from PIL import Image
import subprocess

def convert_and_rename_images(folder_path):
    image_formats = [".webp", ".jpg", ".jpeg", ".bmp", ".tiff",'png']
    avif_format = ".avif"
    
    image_counter = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            original_path = os.path.join(root, filename)
            
            if any(filename.endswith(format) for format in image_formats):
                png_path = os.path.splitext(original_path)[0] + ".png"
                with Image.open(original_path) as img:
                    img.save(png_path, "PNG")
                if not filename.endswith(".png"):
                    os.remove(original_path)
                # Umbenennen des frisch konvertierten Bildes
                rename_image(png_path, root, image_counter)
                image_counter += 1
            elif filename.endswith(avif_format):
                png_path = os.path.splitext(original_path)[0] + ".png"
                subprocess.run(["ffmpeg", "-i", original_path, png_path])
                if not filename.endswith(".png"):
                    os.remove(original_path)
                # Umbenennen des frisch konvertierten Bildes
                rename_image(png_path, root, image_counter)
                image_counter += 1

def rename_image(image_path, root_folder, counter):
    project_name = os.path.basename(os.path.dirname(root_folder))
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
