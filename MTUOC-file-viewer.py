#    MTUOC-file-viewer
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
from tkinter import filedialog
import threading

class LargeFileViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("MTUOC file viewer")
        self.root.geometry("1024x768")  # Ajustar tamaño inicial de la ventana
        
        self.file_path = None
        self.chunk_size = 1024 * 64  # Tamaño del fragmento (64 KB)
        self.cat_running = False
        self.more_position = 0  # Posición para el botón More
        self.tail_position = None  # Posición para el botón Tail

        # Widgets
        self.text_area = tk.Text(self.root, wrap="none", height=25, width=80)
        self.text_area.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.scrollbar_y = tk.Scrollbar(self.text_area, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side="right", fill="y")
        
        self.scrollbar_x = tk.Scrollbar(self.text_area, orient="horizontal", command=self.text_area.xview)
        self.text_area.configure(xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_x.pack(side="bottom", fill="x")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.open_button = tk.Button(self.button_frame, text="Select file", command=self.open_file)
        self.open_button.pack(side="left", padx=5)

        self.cat_button = tk.Button(self.button_frame, text="Cat", command=self.start_cat)
        self.cat_button.pack(side="left", padx=5)

        self.more_button = tk.Button(self.button_frame, text="More", command=self.more)
        self.more_button.pack(side="left", padx=5)

        self.tail_button = tk.Button(self.button_frame, text="Tail", command=self.tail)
        self.tail_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_cat)
        self.stop_button.pack(side="left", padx=5)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*"),("Text files", "*.txt")])
        self.text_area.delete("1.0", tk.END)
        self.more_position = 0
        self.tail_position = None

    def display_chunk(self, chunk):
        self.text_area.insert(tk.END, chunk)
        self.text_area.see(tk.END)

    def start_cat(self):
        if not self.file_path:
            return
        self.cat_running = True
        threading.Thread(target=self.cat).start()

    def cat(self):
        with open(self.file_path, "r", encoding="utf-8", errors="ignore") as f:
            while self.cat_running:
                chunk = f.read(self.chunk_size)
                if not chunk:
                    break
                self.text_area.insert(tk.END, chunk)
                self.text_area.see(tk.END)
                self.text_area.update()

    def stop_cat(self):
        self.cat_running = False

    def more(self):
        if not self.file_path:
            return
        self.stop_cat()
        with open(self.file_path, "r", encoding="utf-8", errors="ignore") as f:
            f.seek(self.more_position)
            chunk = f.read(self.chunk_size)
            if chunk:
                self.more_position = f.tell()  # Actualizar posición para el próximo clic
                self.display_chunk(chunk)

    def tail(self):
        if not self.file_path:
            return
        self.stop_cat()
        with open(self.file_path, "rb") as f:
            if self.tail_position is None:
                f.seek(0, 2)  # Ir al final del archivo
                self.tail_position = f.tell()

            read_size = min(self.chunk_size, self.tail_position)
            self.tail_position -= read_size
            f.seek(self.tail_position, 0)
            chunk = f.read(read_size).decode("utf-8", errors="ignore")

            self.text_area.insert("1.0", chunk)  # Insertar al principio del área de texto
            self.text_area.see("1.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = LargeFileViewer(root)
    root.mainloop()
