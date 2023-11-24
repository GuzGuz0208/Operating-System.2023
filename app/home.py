import tkinter as tk
import time
from PIL import Image, ImageTk
import subprocess

def actualizar_titulo():
    hora_actual = time.strftime("%H:%M:%S")
    fecha_actual = time.strftime("%d/%m/%Y")
    ventana.title(f"{fecha_actual}   {hora_actual}")
    ventana.after(1000, actualizar_titulo)  # Actualizar cada segundo

# Función para abrir una aplicación
def abrir_aplicacion(nombre):
    ventana_app = tk.Toplevel()
    ventana_app.title(nombre)
    ventana_app.geometry("800x600")

# Función para abrir el archivo explore.py
def abrir_explorador():
    subprocess.Popen(["python3", "explore.py"])

def abrir_calculadora():
    subprocess.Popen(["python3", "calculator.py"])

def abrir_editor():
    subprocess.Popen(["python3", "editortxt.py"])

# Crear la ventana principal del escritorio
ventana = tk.Tk()
ventana.title("Simulación de Escritorio")

# Configurar el tamaño de la ventana para que se maximice en Linux
ventana.attributes('-zoomed', True)  # Maximizar la ventana en Linux

# Cargar una imagen de fondo
ruta_fondo = "img/fondo.jpg"
imagen_fondo = Image.open(ruta_fondo)  # Reemplaza "fondo.jpg" con tu propia imagen
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear una etiqueta para mostrar la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(relwidth=1, relheight=1)

# Crear iconos para las aplicaciones
aplicaciones = ["Explorador de Archivos", "Calculadora", "Editor de Texto"]

for i, app in enumerate(aplicaciones):
    if app == "Explorador de Archivos":
        icono = tk.Button(ventana, text=app, command=abrir_explorador)
    elif app == "Calculadora":
        icono = tk.Button(ventana, text=app, command=abrir_calculadora)
    elif app == "Editor de Texto":
        icono = tk.Button(ventana, text=app, command=abrir_editor)
    else:
        icono = tk.Button(ventana, text=app, command=lambda app=app: abrir_aplicacion(app))
    icono.grid(row=i // 3, column=i % 3)

# Iniciar el bucle principal de la interfaz gráfica
ventana.after(0, actualizar_titulo)  # Actualizar el título al iniciar
ventana.mainloop()