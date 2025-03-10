import tkinter as tk
from tkinter import filedialog

def select_file():
    """Opens a file dialog to select a file and sets the file path in the entry."""
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)
        count_file_contents(file_path)

def count_file_contents(file_path):
    """Counts lines, words, and characters in the file without loading it all into memory."""
    try:
        line_count = word_count = char_count = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)

        lines_entry.delete(0, tk.END)
        lines_entry.insert(0, str(line_count))

        words_entry.delete(0, tk.END)
        words_entry.insert(0, str(word_count))

        chars_entry.delete(0, tk.END)
        chars_entry.insert(0, str(char_count))
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not process file: {e}")

# Create main application window
root = tk.Tk()
root.title("MTUOC word count")

# File path entry and button
file_path_label = tk.Label(root, text="File Path:")
file_path_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1, padx=10, pady=10)

select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.grid(row=0, column=2, padx=10, pady=10)

# Results: lines, words, characters
lines_label = tk.Label(root, text="Lines:")
lines_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

lines_entry = tk.Entry(root)
lines_entry.grid(row=1, column=1, padx=10, pady=10)

words_label = tk.Label(root, text="Words:")
words_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

words_entry = tk.Entry(root)
words_entry.grid(row=2, column=1, padx=10, pady=10)

chars_label = tk.Label(root, text="Characters:")
chars_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

chars_entry = tk.Entry(root)
chars_entry.grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
