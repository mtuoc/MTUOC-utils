import tkinter as tk
from tkinter import filedialog, messagebox

def select_file(entry):
    """Open file dialog to select a file and set its path to the entry widget."""
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def select_output_file(entry):
    """Open file dialog to select or create an output file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def process_files(input1_path, input2_path, output_path):
    """Process the two input files line by line and write the combined unique lines to the output file."""
    try:
        # Use a set to track unique combined lines
        with open(input1_path, 'r') as file1, open(input2_path, 'r') as file2, open(output_path, 'w') as outfile:
            while 1:
                line1 = file1.readline().strip()
                line2 = file2.readline().strip()
                if not line1:
                    break
                
                combined_line = f"{line1}\t{line2}"
                outfile.write(combined_line + "\n")

        messagebox.showinfo("Success", "The files have been processed successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_gui():
    """Create the GUI for the file processing application."""
    root = tk.Tk()
    root.title("MTUOC Moses2tabtxtGUI")

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