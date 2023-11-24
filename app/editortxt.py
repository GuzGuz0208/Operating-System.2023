import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import os

# Ruta de la carpeta deseada
ruta_carpeta = "../home/docs"
archivo_abierto = None  # Para rastrear el archivo actual

def abrir_archivo():
    global archivo_abierto
    archivo = filedialog.askopenfile(initialdir=ruta_carpeta, filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        archivo_abierto = archivo
        contenido.delete("1.0", "end")
        contenido.insert("1.0", archivo.read())

def guardar_archivo():
    global archivo_abierto
    if archivo_abierto:
        archivo_abierto.close()  # Cerrar el archivo anterior
    archivo = filedialog.asksaveasfile(initialdir=ruta_carpeta, filetypes=[("Archivos de texto", "*.txt")], mode="w")
    if archivo:
        archivo_abierto = archivo
        archivo.write(contenido.get("1.0", "end"))

def eliminar():
    global archivo_abierto
    if archivo_abierto:
        archivo_abierto.close()
        os.remove(archivo_abierto.name)
        archivo_abierto = None  # Establecer archivo_abierto como None
    contenido.delete("1.0", "end")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")

# Crear un menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# Menú Archivo
menu_archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Eliminar", command=eliminar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_archivo.add_separator()

# Crear un widget de texto para editar o ver el contenido del archivo
contenido = scrolledtext.ScrolledText(ventana)
contenido.pack(fill="both", expand=True)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()