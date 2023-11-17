import tkinter as tk
from tkinter import Entry, Button, Label, Canvas, Scrollbar, Frame
import os
import random
from PIL import Image, ImageTk
import json

# Path to the cache file
cache_path = 'dataset_cache.json'

# This Python script creates a graphical user interface (GUI) application that allows users to navigate
# through a structured dataset of projects. Each project is expected to be in its own directory within
# the main dataset directory. Inside each project directory, there should be subdirectories for characters,
# and an 'output' directory containing model files. Model files should follow the naming convention
# '[ProjectName]_[SequentialNumber].safetensors'. The GUI displays cards for each project and allows
# the user to view character images (if available) and lists of models. Users can search for projects by name
# and refresh the displayed data.
#
# The folder structure should be as follows:
# Dataset/
# ├── ProjectA/
# │   ├── Character1/
# │   ├── Character2/
# │   ├── ...
# │   └── output/
# │       ├── ProjectA_1.safetensors
# │       ├── ProjectA_2.safetensors
# │       └── ...
# ├── ProjectB/
# │   ├── Character1/
# │   ├── Character2/
# │   ├── ...
# │   └── output/
# │       ├── ProjectB_1.safetensors
# │       ├── ProjectB_2.safetensors
# │       └── ...
# └── ...
#
# To use the application, set 'dataset_path' to the file system path of your main dataset directory.
# For example:
# dataset_path = 'C:\\Users\\YourName\\Documents\\Dataset'
# or
# dataset_path = '/home/yourname/Dataset'
#
# The application includes a caching system to speed up the loading process. Upon the first run, it creates
# a 'dataset_cache.json' file which stores the structure of the dataset. Subsequent runs of the application
# will load this cache to display the data quickly. Users can force a refresh of the data, which will
# update the cache file with any changes made to the dataset directory.


def save_to_cache(data, path):
    # Saves data to a cache file in JSON format
    with open(path, 'w') as cache_file:
        json.dump(data, cache_file, indent=4)

def load_from_cache(path):
    # Loads data from a cache file if it exists
    try:
        with open(path, 'r') as cache_file:
            return json.load(cache_file)
    except FileNotFoundError:
        return None

def read_folder_structure(path):
    # Reads the folder structure and creates a dictionary with project data
    projects = {}
    for project_name in os.listdir(path):
        project_path = os.path.join(path, project_name)
        if os.path.isdir(project_path):
            projects[project_name] = {'characters': [], 'models': [], 'preview': None}
            for item in os.listdir(project_path):
                item_path = os.path.join(project_path, item)
                if os.path.isdir(item_path) and item != 'output':
                    projects[project_name]['characters'].append(item)
                    image_files = [file for file in os.listdir(item_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
                    if image_files:
                        preview_image = random.choice(image_files)
                        projects[project_name]['preview'] = os.path.join(item_path, preview_image)
                elif item == 'output':
                    models_path = os.path.join(item_path)
                    for model in os.listdir(models_path):
                        if model.endswith('.safetensors'):
                            projects[project_name]['models'].append(os.path.join(models_path, model))
    return projects

def create_image_popup(image_path):
    # Creates a popup window to display a larger image
    popup = tk.Toplevel()
    popup.title('Image Preview')
    img = Image.open(image_path)
    img.thumbnail((800, 800), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(popup, image=photo)
    label.image = photo  # Keep a reference!
    label.pack()

def create_models_popup(project_data):
    # Creates a popup window to display available models for a project
    popup = tk.Toplevel()
    popup.title('Models')
    for model_path in project_data['models']:
        model_name = os.path.basename(model_path)
        btn_model = tk.Button(popup, text=model_name, command=lambda m=model_path: os.startfile(os.path.dirname(m)))
        btn_model.pack()

def refresh_data(root, scrollable_frame, projects):
    # Refreshes the GUI to display project cards
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    create_gui(root, scrollable_frame, projects)

def filter_projects(search_term, all_projects):
    # Filters projects based on a search term
    return {name: data for name, data in all_projects.items() if search_term.lower() in name.lower()}

def update_project_display(root, scrollable_frame, projects, search_term=''):
    # Updates the project display based on a search term or resets the display
    if search_term:
        filtered_projects = filter_projects(search_term, projects)
        refresh_data(root, scrollable_frame, filtered_projects)
    else:
        refresh_data(root, scrollable_frame, projects)

def create_gui(root, scrollable_frame, projects):
    # Creates the GUI layout, including a search bar and buttons
    if not hasattr(root, 'search_frame'):
        root.search_frame = Frame(root, bg='grey20')
        root.search_frame.pack(side='top', fill='x')
        root.search_entry = tk.Entry(root.search_frame)
        root.search_entry.pack(side='left', padx=(10, 0), pady=10)
        root.search_button = tk.Button(root.search_frame, text='Search', command=lambda: update_project_display(root, scrollable_frame, projects, root.search_entry.get()))
        root.search_button.pack(side='left', padx=10)
        root.reset_button = tk.Button(root.search_frame, text='Reset', command=lambda: update_project_display(root, scrollable_frame, projects))
        root.reset_button.pack(side='left', padx=10)

    # Variables for grid layout
    rows, cols = 6, 5
    row_count = col_count = 0

    # Create project cards
    for project_name, project_data in projects.items():
        card_frame = Frame(scrollable_frame, bg='grey20', borderwidth=2, relief="raised")
        card_frame.grid(row=row_count, column=col_count, padx=10, pady=10, sticky='nsew')
        col_count += 1
        if col_count == cols:
            col_count = 0
            row_count += 1

        label = Label(card_frame, text=project_name, bg='grey20', fg='white')
        label.pack()
        label.bind('<Button-1>', lambda e, p=project_data: create_models_popup(p))

        if project_data['preview']:
            img = Image.open(project_data['preview'])
            img.thumbnail((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label_img = Label(card_frame, image=photo, bg='grey20')
            label_img.image = photo  # Keep a reference!
            label_img.pack()
            label_img.bind('<Button-1>', lambda e, i=project_data['preview']: create_image_popup(i))

        btn_show = Button(card_frame, text='Show in folder', bg='grey30', fg='white', 
                             command=lambda proj_path=project_data['preview']: os.startfile(os.path.dirname(proj_path)))
        btn_show.pack()

    for i in range(rows):
        scrollable_frame.grid_rowconfigure(i, weight=1)
    for i in range(cols):
        scrollable_frame.grid_columnconfigure(i, weight=1)

    # Add a button to update the data
    btn_refresh = Button(root, text='Update Data', command=lambda: refresh_data(root, scrollable_frame, read_folder_structure(dataset_path)))
    btn_refresh.pack(side='bottom')

def main():
    # Main function to run the application
    root = tk.Tk()
    root.title('Project Explorer')
    root.configure(bg='black')
    root.geometry('1200x800')  # Default size to display 6x5 cards

    canvas = Canvas(root, borderwidth=0, bg='black')
    scrollable_frame = Frame(canvas, bg='black')
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    # Load cached data or create structure if no cache is present
    project_structure = load_from_cache(cache_path)
    if project_structure is None:
        project_structure = read_folder_structure(dataset_path)
        save_to_cache(project_structure, cache_path)

    create_gui(root, scrollable_frame, project_structure)

    root.mainloop()

if __name__ == "__main__":
    dataset_path = 'X:\\'  # Replace this with the actual path to your dataset
    main()
