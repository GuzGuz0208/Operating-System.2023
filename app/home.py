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

# Funciones para abrir aplicaciones específicas
def abrir_explorador():
    subprocess.Popen(["python3", "app/explore.py"])

def abrir_calculadora():
    subprocess.Popen(["python3", "app/calculator.py"])

def abrir_editor():
    subprocess.Popen(["python3", "app/editortxt.py"])

def abrir_monitor():
    subprocess.Popen(["python3", "app/monitor.py"])

def abrir_navegador():
    subprocess.Popen(["python3", "app/browser.py"])

def abrir_reproductor():
    subprocess.Popen(["python3", "app/reproductor.py"])

def abrir_video():
    subprocess.Popen(["python3", "app/video.py"])

def abrir_visordoc():
    subprocess.Popen(["python3", "app/visor.py"])

# Crear la ventana principal del escritorio
ventana = tk.Tk()
ventana.title("Simulación de Escritorio")

# Configurar el tamaño de la ventana para que se maximice en Linux
ventana.attributes('-zoomed', True)  # Maximizar la ventana en Linux

# Cargar una imagen de fondo
ruta_fondo = "app/img/fondo.jpg"
imagen_fondo = Image.open(ruta_fondo)  # Reemplaza "fondo.jpg" con tu propia imagen
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear una etiqueta para mostrar la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(relwidth=1, relheight=1)

# Crear iconos para las aplicaciones
aplicaciones = ["Explorador de Archivos", "Calculadora", "Editor de Texto", "Monitor de Recursos", "Navegador Web", 
                "Reproductor de Audio", "Reproductor de Video", "Visor de Imágenes"]

for i, app in enumerate(aplicaciones):
    if app == "Explorador de Archivos":
        icono = tk.Button(ventana, text=app, command=abrir_explorador)
    elif app == "Calculadora":
        icono = tk.Button(ventana, text=app, command=abrir_calculadora)
    elif app == "Editor de Texto":
        icono = tk.Button(ventana, text=app, command=abrir_editor)
    elif app == "Monitor de Recursos":
        icono = tk.Button(ventana, text=app, command=abrir_monitor)
    elif app == "Navegador Web":
        icono = tk.Button(ventana, text=app, command=abrir_navegador)
    elif app == "Reproductor de Audio":
        icono = tk.Button(ventana, text=app, command=abrir_reproductor)
    elif app == "Reproductor de Video":
        icono = tk.Button(ventana, text=app, command=abrir_video)
    elif app == "Visor de Imágenes":
        icono = tk.Button(ventana, text=app, command=abrir_visordoc)
    else:
        icono = tk.Button(ventana, text=app, command=lambda app=app: abrir_aplicacion(app))
    icono.grid(row=i // 3, column=i % 3)

# Iniciar el bucle principal de la interfaz gráfica
ventana.after(0, actualizar_titulo)  # Actualizar el título al iniciar
ventana.mainloop()