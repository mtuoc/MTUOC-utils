#    MTUOC-Moses2tabtxt-GUI
#    Copyright (C) 2025  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import filedialog, messagebox
import codecs
import os


def select_file(entry):
    """Open file dialog to select a file and set its path to the entry widget."""
    file_path = filedialog.askopenfilename()
    if file_path:
        norm_file_path=os.path.normpath(file_path)
        entry.delete(0, tk.END)
        entry.insert(0, norm_file_path)

def select_output_file(entry):
    """Open file dialog to select or create an output file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        norm_file_path=os.path.normpath(file_path)
        entry.delete(0, tk.END)
        entry.insert(0, norm_file_path)

def process_files(input1_path, input2_path, output_path):
    """Process the two input files line by line and write the combined unique lines to the output file."""
    try:
        # Use a set to track unique combined lines
        with codecs.open(input1_path, 'r',encoding="utf-8") as file1, codecs.open(input2_path, 'r',encoding="utf-8") as file2, codecs.open(output_path, 'w',encoding="utf-8") as outfile:
            for line1 in file1:
                line1 = line1.strip()
                line2 = file2.readline().strip()
                combined_line = f"{line1}\t{line2}"
                outfile.write(combined_line + "\n")
        messagebox.showinfo("Success", "The files have been processed successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_gui():
    """Create the GUI for the file processing application."""
    root = tk.Tk()
    root.title("MTUOC Moses2tabtxt GUI (aka paste)")

    # Input file 1
    tk.Label(root, text="Input File 1:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    input1_entry = tk.Entry(root, width=50)
    input1_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_file(input1_entry)).grid(row=0, column=2, padx=5, pady=5)

    # Input file 2
    tk.Label(root, text="Input File 2:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    input2_entry = tk.Entry(root, width=50)
    input2_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_file(input2_entry)).grid(row=1, column=2, padx=5, pady=5)

    # Output file
    tk.Label(root, text="Output File:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_file(output_entry)).grid(row=2, column=2, padx=5, pady=5)

    # Process button
    tk.Button(root, text="Process", command=lambda: process_files(input1_entry.get(), input2_entry.get(), output_entry.get())).grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()