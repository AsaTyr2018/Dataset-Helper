# Steps Calculator with Recommendations
# This tool calculates the number of training steps based on images, repeats, epochs, and batch size.
# Additionally, it provides recommendations for repeats and epochs based on the number of images.


import tkinter as tk
from tkinter import ttk

# Function to calculate steps
def calculate_steps():
    try:
        images = int(images_entry.get())
        repeats = int(repeats_entry.get())
        epochs = int(epochs_entry.get())
        batch_size = int(batch_size_entry.get())
        
        steps = (images * repeats * epochs) // batch_size
        result_label.config(text=f"Steps: {steps}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

def recommend_configuration(*args):
    try:
        images = int(images_entry.get())
        recommended_repeats, recommended_epochs = get_recommendation(images)
        recommendation_label.config(text=f"Recommended: {recommended_repeats} Repeats & {recommended_epochs} Epochs")
    except ValueError:
        recommendation_label.config(text="Recommended: - Repeats & - Epochs")

def get_recommendation(images):
    if images <= 10:
        return 10, 20
    elif images <= 20:
        return 10, 10
    elif images <= 100:
        return 3, 10
    elif images <= 400:
        return 1, 10
    else:
        return 1, 10

# Create the main window
root = tk.Tk()
root.title("Steps Calculator with Recommendation")

# Create and pack widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Images:").grid(row=0, column=0, sticky=tk.W, pady=5)
images_entry = ttk.Entry(frame)
images_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
images_entry.bind('<KeyRelease>', recommend_configuration)  # Update recommendation on key release

ttk.Label(frame, text="Repeats:").grid(row=1, column=0, sticky=tk.W, pady=5)
repeats_entry = ttk.Entry(frame)
repeats_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

ttk.Label(frame, text="Epochs:").grid(row=2, column=0, sticky=tk.W, pady=5)
epochs_entry = ttk.Entry(frame)
epochs_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

ttk.Label(frame, text="Batch Size:").grid(row=3, column=0, sticky=tk.W, pady=5)
batch_size_entry = ttk.Entry(frame)
batch_size_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate_steps)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="Steps: -")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

recommendation_label = ttk.Label(frame, text="Recommended: - Repeats & - Epochs")
recommendation_label.grid(row=6, column=0, columnspan=2, pady=5)

# Configure column and row weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
