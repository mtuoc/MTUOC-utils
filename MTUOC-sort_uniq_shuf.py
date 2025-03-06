import tkinter as tk
from tkinter import filedialog, messagebox
import random

def select_input_file(input_entry):
    """Open file dialog to select an input file and set its path to the entry widget."""
    file_path = filedialog.askopenfilename()
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def select_output_file(output_entry):
    """Open file dialog to select or create an output file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def process_file(input_path, output_path):
    """Process the input file to output unique lines in random order using memory."""
    try:
        if not input_path or not output_path:
            messagebox.showwarning("Warning", "Please specify both input and output files.")
            return

        with open(input_path, 'r', encoding='utf-8') as infile:
            # Read all lines, strip whitespace, and deduplicate using a set
            unique_lines = list(set(line.strip() for line in infile if line.strip()))

        # Shuffle the unique lines
        random.shuffle(unique_lines)

        # Write shuffled lines to the output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write("\n".join(unique_lines) + "\n")

        messagebox.showinfo("Success", "The file has been processed successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_gui():
    """Create the GUI for the unique line randomizer application."""
    root = tk.Tk()
    root.title("MTUOC-sort_uniq_shuf")

    # Input file
    tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    input_entry = tk.Entry(root, width=50)
    input_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_input_file(input_entry)).grid(row=0, column=2, padx=5, pady=5)

    # Output file
    tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_file(output_entry)).grid(row=1, column=2, padx=5, pady=5)

    # Process button
    tk.Button(root, text="Process", command=lambda: process_file(input_entry.get(), output_entry.get())).grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()