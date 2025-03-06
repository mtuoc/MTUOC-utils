import tkinter as tk
from tkinter import filedialog, messagebox

def add_input_file(file_listbox):
    """Open file dialog to select a file and add its path to the listbox.""" 
    file_path = filedialog.askopenfilename()
    if file_path:
        file_listbox.insert(tk.END, file_path)

def clear_input_files(file_listbox):
    """Clear all files from the listbox."""
    file_listbox.delete(0, tk.END)

def select_output_file(output_entry):
    """Open file dialog to select or create an output file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def concatenate_files(file_listbox, output_path):
    """Concatenate all input files and write to the output file."""
    try:
        input_files = file_listbox.get(0, tk.END)

        if not input_files:
            messagebox.showwarning("Warning", "No input files selected.")
            return

        if not output_path:
            messagebox.showwarning("Warning", "No output file specified.")
            return

        with open(output_path, 'w') as outfile:
            for input_file in input_files:
                with open(input_file, 'r') as infile:
                    outfile.write(infile.read())

        messagebox.showinfo("Success", "Files have been concatenated successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_gui():
    """Create the GUI for the file concatenation application."""
    root = tk.Tk()
    root.title("MTUOC concat")

    # Input files section
    tk.Label(root, text="Input Files:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    file_listbox = tk.Listbox(root, width=50, height=10)
    file_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    tk.Button(root, text="Add File", command=lambda: add_input_file(file_listbox)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tk.Button(root, text="Clear Files", command=lambda: clear_input_files(file_listbox)).grid(row=2, column=1, padx=5, pady=5, sticky="e")

    # Output file section
    tk.Label(root, text="Output File:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=4, column=0, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_file(output_entry)).grid(row=4, column=1, padx=5, pady=5)

    # Concatenate button
    tk.Button(root, text="Concatenate", command=lambda: concatenate_files(file_listbox, output_entry.get())).grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
