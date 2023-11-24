import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

# Ruta inicial para la carga principal
ruta_inicial = "../home/"

def abrir_directorio():
    global carpeta_actual
    directorio = filedialog.askdirectory(initialdir=ruta_inicial)
    if directorio:
        carpeta_actual = directorio
        cargar_contenido(carpeta_actual)

def cargar_contenido(directorio):
    lista_directorio.delete(*lista_directorio.get_children())
    for item in os.listdir(directorio):
        lista_directorio.insert('', 'end', text=item, values=(os.path.join(directorio, item),))

def abrir_archivo(event):
    seleccion = lista_directorio.selection()
    if seleccion:
        archivo_seleccionado = lista_directorio.item(seleccion)['values'][0]
        if os.path.isfile(archivo_seleccionado):
            with open(archivo_seleccionado, 'r') as archivo:
                contenido_text.delete('1.0', 'end')
                contenido_text.insert('1.0', archivo.read())

ventana = tk.Tk()
ventana.title("Explorador de Archivos")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

menu_archivo = tk.Menu(menu)
menu.add_cascade(label="Opciones", menu=menu_archivo)
menu_archivo.add_command(label="Abrir Directorio", command=abrir_directorio)

frame_explorador = ttk.Frame(ventana)
frame_explorador.pack(fill="both", expand=True, side="left")

lista_directorio = ttk.Treeview(frame_explorador, columns=("ruta",))
lista_directorio.heading('#1', text="Archivo/Directorio")
lista_directorio.heading('ruta', text="Ruta")
lista_directorio.pack(fill="both", expand=True, side="left")

scrollbar = ttk.Scrollbar(frame_explorador, orient="vertical", command=lista_directorio.yview)
scrollbar.pack(side="right", fill="y")
lista_directorio.config(yscrollcommand=scrollbar.set)

frame_contenido = ttk.Frame(ventana)
frame_contenido.pack(fill="both", expand=True, side="right")

contenido_text = tk.Text(frame_contenido)
contenido_text.pack(fill="both", expand=True)

carpeta_actual = ruta_inicial
cargar_contenido(carpeta_actual)

lista_directorio.bind("<Double-1>", abrir_archivo)

ventana.mainloop()
