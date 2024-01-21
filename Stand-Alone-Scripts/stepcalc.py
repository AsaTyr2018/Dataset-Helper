import tkinter as tk
from tkinter import ttk

def calculate_repeats():
    try:
        num_images = int(images_entry.get())
        num_epochs = int(epochs_entry.get())
        batch_size = int(batch_size_entry.get())
        target_steps_per_epoch = 1500

        # Calculate the number of repeats needed
        repeats = (target_steps_per_epoch * batch_size) / (num_images * num_epochs)
        repeats = int(repeats) if repeats.is_integer() else int(repeats) + 1  # Round up

        # Display the result
        result_label.config(text=f"Required Repeats: {repeats}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers only.")

# Create the main window
window = tk.Tk()
window.title("Lora Training Calculator")
window.configure(background="#f0f0f0")

# Create and grid the input fields and labels
images_label = ttk.Label(window, text="Number of Images:", background="#f0f0f0")
images_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

images_entry = ttk.Entry(window)
images_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

epochs_label = ttk.Label(window, text="Number of Epochs:", background="#f0f0f0")
epochs_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

epochs_entry = ttk.Entry(window)
epochs_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

batch_size_label = ttk.Label(window, text="Batch Size:", background="#f0f0f0")
batch_size_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

batch_size_entry = ttk.Entry(window)
batch_size_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

# Create and grid the calculate button
calculate_button = ttk.Button(window, text="Calculate Repeats", command=calculate_repeats)
calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

# Create and grid the result label
result_label = ttk.Label(window, text="", background="#f0f0f0")
result_label.grid(column=0, row=4, columnspan=2)

# Powered by Lenz-Service Network label
powered_by_label = ttk.Label(window, text="Powered by Lenz-Service Network", background="#f0f0f0", font=("Arial", 10, "italic"))
powered_by_label.grid(column=0, row=5, columnspan=2, pady=5)

# Set the grid column configuration
window.columnconfigure(1, weight=1)

# Run the application
window.mainloop()
