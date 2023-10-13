import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import scrolledtext

def process_text():
    raw_text = text_input.get("1.0", tk.END)
    lines = raw_text.split("\n")

    words = []
    for line in lines:
        if ":" in line:
            word = line.split(":")[0].strip()
            words.append(word)

    converted_content = ", ".join(words)

    text_input.delete("1.0", tk.END)
    text_input.insert(tk.INSERT, converted_content)

def create_text_processor_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Text Processor")

    global text_input  # Definieren Sie text_input als global, damit er in der process_text-Funktion erkannt wird
    text_input = scrolledtext.ScrolledText(tab, width=60, height=15)
    text_input.pack(pady=10, padx=10)

    process_button = tk.Button(tab, text="Process Text", command=process_text)
    process_button.pack(pady=5)
