import tkinter as tk
from tkinter import ttk
from modules.tag_removal import create_tag_removal_tab
from modules.folder_creation import create_folder_creation_tab
from modules.image_conversion import create_image_conversion_tab

def open_git_link():
    import webbrowser
    webbrowser.open("https://github.com/AsaTyr2018/Dataset-Helper")

# Erstellen Sie das Hauptfenster
root = tk.Tk()
root.title("Dataset-Helper by Lenz-Service Network")

# Setzen Sie die Standardgröße auf 800x600
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

# Fügen Sie die Tab-Inhalte in der gewünschten Reihenfolge hinzu
create_folder_creation_tab(notebook)
create_image_conversion_tab(notebook)
create_tag_removal_tab(notebook)

# Erstellen Sie ein anklickbares Label für den Git-Link
git_label = tk.Label(root, text="Visit Git", cursor="hand2")
git_label.pack(anchor="w", padx=10, pady=10)
git_label.bind("<Button-1>", lambda event: open_git_link())

root.mainloop()
