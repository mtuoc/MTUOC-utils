import sqlite3
import random
import os
import codecs
import tkinter as tk
from tkinter import filedialog, messagebox

def procesar():
    db_path = "temp_database.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE dades (linia TEXT)')
    
    arxiu_entrada = entry_arxiu_entrada.get()
    arxiu_sortida = entry_arxiu_sortida.get()
    sortida=codecs.open(arxiu_sortida,"w",encoding="utf-8")
    if not arxiu_entrada or not arxiu_sortida:
        messagebox.showerror("Error", "Input and output files should be given.")
        return
    
    arxiu_entrada_norm=os.path.normpath(arxiu_entrada)
    arxiu_sortida_norm=os.path.normpath(arxiu_sortida)
    
    with codecs.open(arxiu_entrada_norm, 'r', encoding="utf-8") as arxiu:
        contlinia=0
        for linia in arxiu:
            linia=linia.strip()
            cursor.execute('INSERT INTO dades (linia) VALUES (?)', (linia,))
            contlinia+=1
            if contlinia==100000:
                conn.commit()
                contlinia=0
        conn.commit()
            
    
    eliminar_reps = var_eliminar_reps.get()
    desordenar = var_desordenar.get()
   
    if eliminar_reps:
        cursor.execute('DELETE FROM dades WHERE ROWID NOT IN (SELECT MIN(ROWID) FROM dades GROUP BY linia)')
        conn.commit()
       
    if desordenar:
        cursor.execute('SELECT * FROM dades ORDER BY RANDOM()')
        for segment in cursor:
            sortida.write(segment[0]+"\n")        
    else:
        cursor.execute('SELECT * FROM dades')
        for segment in cursor:
            sortida.write(segment[0]+"\n")
            
    conn.close()
    os.remove(db_path)

# Funció per obrir un diàleg per seleccionar un arxiu
def obrir_arxiu_entrada():
    arxiu = filedialog.askopenfilename(title="Selecciona l'arxiu d'entrada", filetypes=[("All files", "*.*")])
    if arxiu:
        entry_arxiu_entrada.delete(0, tk.END)
        entry_arxiu_entrada.insert(0, arxiu)

# Funció per obrir un diàleg per seleccionar un arxiu de sortida
def obrir_arxiu_sortida():
    arxiu = filedialog.asksaveasfilename(title="Selecciona l'arxiu de sortida", filetypes=[("All files", "*.*")])
    if arxiu:
        entry_arxiu_sortida.delete(0, tk.END)
        entry_arxiu_sortida.insert(0, arxiu)



# Crear la finestra principal
root = tk.Tk()
root.title("MTUOC sort uniq shuf")

# Crear components de la interfície
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entrada per al fitxer d'entrada
label_entrada = tk.Label(frame, text="Input file:")
label_entrada.grid(row=0, column=0, sticky="w", pady=5)
entry_arxiu_entrada = tk.Entry(frame, width=50)
entry_arxiu_entrada.grid(row=0, column=1, padx=5, pady=5)
btn_obrir_entrada = tk.Button(frame, text="Open", command=obrir_arxiu_entrada)
btn_obrir_entrada.grid(row=0, column=2, padx=5, pady=5)

# Entrada per al fitxer de sortida
label_sortida = tk.Label(frame, text="Output file:")
label_sortida.grid(row=1, column=0, sticky="w", pady=5)
entry_arxiu_sortida = tk.Entry(frame, width=50)
entry_arxiu_sortida.grid(row=1, column=1, padx=5, pady=5)
btn_obrir_sortida = tk.Button(frame, text="Save", command=obrir_arxiu_sortida)
btn_obrir_sortida.grid(row=1, column=2, padx=5, pady=5)

# Opció per eliminar repeticions
var_eliminar_reps = tk.BooleanVar()
check_eliminar_reps = tk.Checkbutton(frame, text="uniq", variable=var_eliminar_reps)
check_eliminar_reps.grid(row=2, columnspan=3, pady=5)

# Opció per desordenar aleatòriament
var_desordenar = tk.BooleanVar()
check_desordenar = tk.Checkbutton(frame, text="shuf", variable=var_desordenar)
check_desordenar.grid(row=3, columnspan=3, pady=5)

# Botó per iniciar el processament
btn_iniciar = tk.Button(frame, text="Go!", command=procesar)
btn_iniciar.grid(row=4, columnspan=3, pady=10)

# Mostrar la finestra
root.mainloop() 