# Dataset Helper by Lenz-Service Network

## Overview:

The Dataset Helper is a versatile tool designed to assist with various dataset management tasks. It provides a graphical user interface (GUI) with multiple functions for tasks like tag removal, folder creation, and image conversion. This README provides an overview of how to use the tool and its sub-functions.

**Simplify Your AI Journey with Seait:**
Are you interested in exploring AI repositories effortlessly? Introducing Seait (**Super Easy AI Installer Tool**), a user-friendly application that simplifies the installation process of AI-related repositories for users. Seait automatically handles the installation process, making it easier for users to access and use AI tools. Discover the power of Seait and unlock a world of AI possibilities. Visit the [Seait Git](https://github.com/diStyApps/seait) to learn more.

## Features

### Tag Removal

The "Tag Removal" function allows you to remove specific tags from text files within a selected folder. 

Here's how to use it:
Click on the "Tag Removal" tab in the GUI.
Enter the folder path containing the text files you want to process.
Enter the tags you want to remove, separated by commas (e.g., tag1,tag2).
Click the "Browse" button to select the folder interactively or manually enter the folder path.
Click the "Check Tags" button to view the existing tags and their counts in the selected folder. This step is optional.
Click the "Remove Tags" button to perform the tag removal. The tool will update you with the total number of tags removed.

### Folder Creation

The "Folder Creation" function allows you to create a predefined folder structure within a specified base directory. 

It generates the following folders:  
Dataset: Contains images and tagging files.  
Output: Contains LoRA files and sample images (if configured).

Here's how to use it:
Click on the "Folder Creation" tab in the GUI.
Enter the base directory where you want to create the folders.
Enter the project name.
Click the "Create Folders" button to generate the folder structure within the specified base directory.

### Image Conversion

The "Image Conversion" function converts various image formats to PNG format. 

Here's how to use it:
Click on the "Image Conversion" tab in the GUI.
Enter the folder path containing the images you want to convert.
Click the "Convert Images to PNG" button to start the conversion process. The tool will convert compatible image formats within the specified folder.

## Getting Started

1. **Installation:** No installation is required. Just download the provided files and make sure you have Python installed.

2. **Dependencies:** Ensure you have the required dependencies installed, including tkinter and Pillow. You can install them using pip:
   ```
   pip install tk
   pip install Pillow

3. Run the Program: Run the main.py file to launch the GUI.
   ```
   python main.py

## System Requirements

- Python 3.x
- Additional libraries as specified in the repository

## Acknowledgments

- [Seait](https://github.com/diStyApps/seait) - Super Easy AI Installer Tool

