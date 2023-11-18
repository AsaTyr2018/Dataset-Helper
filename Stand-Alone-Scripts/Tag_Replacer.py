import tkinter as tk
from tkinter import filedialog, messagebox
import os

# This script creates a simple GUI application to replace text in all '.txt' files within a chosen directory.
# User can specify the directory, the text to be replaced, and the new text to replace with.
# After replacements are done, a message box will confirm the completion.

def replace_in_files(folder_path, old_text, new_text):
    # Iterate through the files in the specified directory
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace the old text with the new text
            content_new = content.replace(old_text, new_text)
            
            # Write the new content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content_new)

def browse_folder():
    # Open a dialog to choose a directory
    folder_path.set(filedialog.askdirectory())

def start_replacement():
    # Start the replacement process
    replace_in_files(folder_path.get(), old_tag.get(), new_tag.get())
    # Notify the user upon completion
    messagebox.showinfo("Completed", "The tags have been replaced.")

# Initialize the GUI
root = tk.Tk()
root.title("Tag Replacer")

# Input fields
folder_path = tk.StringVar()
old_tag = tk.StringVar()
new_tag = tk.StringVar()

# Setup the GUI layout
tk.Label(root, text="Folder Path:").grid(row=0)
tk.Entry(root, textvariable=folder_path, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(root, text="Tag to replace:").grid(row=1)
tk.Entry(root, textvariable=old_tag, width=50).grid(row=1, column=1)

tk.Label(root, text="Replace with:").grid(row=2)
tk.Entry(root, textvariable=new_tag, width=50).grid(row=2, column=1)

tk.Button(root, text="Replace", command=start_replacement).grid(row=3, column=1)

# Start the GUI event loop
root.mainloop()
