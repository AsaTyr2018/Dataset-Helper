import tkinter as tk
from tkinter import ttk
import os

def create_folders(base_dir, project_name, folders):
    project_dir = os.path.join(base_dir, project_name)
    for folder in folders:
        full_path = os.path.join(project_dir, folder)
        os.makedirs(full_path, exist_ok=True)
    return project_dir

def create_folder_creation_tab(notebook):
    folder_creation_frame = ttk.Frame(notebook)
    notebook.add(folder_creation_frame, text="Folder Creation")

    base_dir_label = tk.Label(folder_creation_frame, text="Base Directory:")
    base_dir_label.pack()
    base_dir_entry = tk.Entry(folder_creation_frame, width=50)
    base_dir_entry.pack()

    project_name_label = tk.Label(folder_creation_frame, text="Project Name:")
    project_name_label.pack()
    project_name_entry = tk.Entry(folder_creation_frame, width=50)
    project_name_entry.pack()

    create_folders_button = tk.Button(folder_creation_frame, text="Create Folders")
    create_folders_button.pack()

    result_label = tk.Label(folder_creation_frame, text="")
    result_label.pack()

    def create_folders_button_click():
        base_dir = base_dir_entry.get()
        project_name = project_name_entry.get()
        folders = [
            "dataset",
            "output",
            "output\sample"
        ]
        created_folders = create_folders(base_dir, project_name, folders)
        result_label.config(text=f"Folders successfully created at {created_folders}")

    create_folders_button.config(command=create_folders_button_click)
