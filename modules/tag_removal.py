import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def remove_tags(folder_path, tags_to_remove):
    total_removed = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                tags_list = content.split(', ')
                initial_tag_count = len(tags_list)
                new_tags_list = [tag for tag in tags_list if tag not in tags_to_remove]
                removed_tags = initial_tag_count - len(new_tags_list)
                total_removed += removed_tags
                new_content = ', '.join(new_tags_list)
                with open(file_path, 'w') as f:
                    f.write(new_content)
    return total_removed

def create_tag_removal_tab(notebook):
    tag_removal_frame = ttk.Frame(notebook)
    notebook.add(tag_removal_frame, text="Tag Removal")

    folder_label = tk.Label(tag_removal_frame, text="Folder Path:")
    folder_label.pack()
    folder_entry = tk.Entry(tag_removal_frame, width=50)
    folder_entry.pack()

    tags_label = tk.Label(tag_removal_frame, text="Tags to Remove (comma-separated):")
    tags_label.pack()
    tags_entry = tk.Entry(tag_removal_frame, width=50)
    tags_entry.pack()

    result_label = tk.Label(tag_removal_frame, text="")
    result_label.pack()

    def browse_folder():
        folder_path = filedialog.askdirectory()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

    def remove_tags_button():
        folder_path = folder_entry.get()
        tags_to_remove = tags_entry.get().split(',')
        tags_to_remove = [tag.strip() for tag in tags_to_remove]

        total_removed = remove_tags(folder_path, tags_to_remove)

        result_label.config(text=f"Tags successfully removed. Total removed: {total_removed}")

    def check_tags_button():
        folder_path = folder_entry.get()
        tags_count = {}

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        content = f.read()
                    tags_list = content.split(', ')
                    for tag in tags_list:
                        tags_count[tag] = tags_count.get(tag, 0) + 1

        # Sortieren Sie die Tags nach der Anzahl der Vorkommen absteigend
        sorted_tags_count = sorted(tags_count.items(), key=lambda x: x[1], reverse=True)
        
        # Erstellen Sie ein Popup-Fenster für die Tags-Anzeige
        popup = tk.Toplevel()
        popup.title("Tags in Folders")
        popup.geometry("400x300")
        popup.resizable(True, True)

        tags_text = tk.Text(popup)
        tags_text.pack(fill="both", expand=True)

        for tag, count in sorted_tags_count:
            tags_text.insert(tk.END, f"{tag}: {count}\n")

    browse_button = tk.Button(tag_removal_frame, text="Browse", command=browse_folder)
    browse_button.pack()

    check_tags_button = tk.Button(tag_removal_frame, text="Check Tags", command=check_tags_button)
    check_tags_button.pack()

    remove_button = tk.Button(tag_removal_frame, text="Remove Tags", command=remove_tags_button)
    remove_button.pack()
