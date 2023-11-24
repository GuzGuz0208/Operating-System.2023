import tkinter as tk
import time
from PIL import Image, ImageTk
from tkinter import font
import subprocess

def iniciar_sesion():
    # Reemplace 'python3' con su comando para ejecutar Python en su sistema
    comando = 'python3 home.py'
    
    try:
        subprocess.Popen(comando, shell=True)
    except Exception as e:
        mensaje_label.config(text=f"Error al iniciar sesión: {e}")
    else:
        mensaje_label.config(text="Inicio de sesión exitoso")
        ventana.destroy()

def actualizar_titulo():
    hora_actual = time.strftime("%H:%M:%S")
    fecha_actual = time.strftime("%d/%m/%Y")
    ventana.title(f"{fecha_actual}   {hora_actual}")
    ventana.after(1000, actualizar_titulo)  # Actualizar cada segundo

def mostrar_contrasena():
    nombre_usuario_button.grid_forget()  # Ocultar el botón de nombre de usuario
    entry_contrasena.grid(row=1, column=0, pady=(centro_y, 10))  # Centrar el campo de contraseña en la fila 1
    boton_iniciar_sesion.grid(row=2, column=0, pady=10)  # Centrar el botón de inicio de sesión en la fila 2

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Configurar el tamaño de la ventana para que se maximice en Linux
ventana.attributes('-zoomed', True)  # Maximizar la ventana en Linux

# Calcular el centro de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
centro_x = ancho_pantalla // 2
centro_y = alto_pantalla // 2

# Crear una fuente personalizada
mi_fuente = font.Font(family="KacstQurn", size=12, weight="bold")

# Cargar una imagen de fondo
ruta_fondo = "img/fondo.jpg"
imagen_fondo = Image.open(ruta_fondo)  # Reemplaza "fondo.jpg" con tu propia imagen
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear una etiqueta para mostrar la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(relwidth=1, relheight=1)

# Cargar un ícono de usuario desde una subcarpeta
ruta_icono = "img/usuario.png"
imagen_usuario = Image.open(ruta_icono)
nuevo_tamano = (175, 100)  # Cambia el tamaño a tu preferencia
imagen_usuario = imagen_usuario.resize(nuevo_tamano)

# Convertir la imagen redimensionada en un objeto ImageTk
imagen_usuario_tk = ImageTk.PhotoImage(imagen_usuario)

# Crear un botón personalizado para el nombre de usuario
nombre_usuario_button = tk.Button(ventana, text="Juan E. Guzmán", font=(mi_fuente),
                                  image=imagen_usuario_tk, compound="left", command=mostrar_contrasena,
                                  bg="#71c55b", activebackground="#4ea93b", fg="white", activeforeground="white")
nombre_usuario_button.grid(row=0, column=0, pady=centro_y-100)  # Centrar el botón en la columna 0

# Crear un campo de contraseña (inicialmente oculto)
entry_contrasena = tk.Entry(ventana, show="*")

# Botón para iniciar sesión (inicialmente oculto)
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", font=(mi_fuente), command=iniciar_sesion)
boton_iniciar_sesion.grid(row=2, column=0, pady=10)  # Centrar el botón de inicio de sesión en la fila 2
boton_iniciar_sesion.grid_forget()

# Etiqueta para mostrar mensajes
mensaje_label = tk.Label(ventana, text="Welcome")
mensaje_label.grid(row=3, column=0, pady=10, padx=centro_x)  # Centrar la etiqueta en la columna 0

# Iniciar el bucle principal de la interfaz gráfica
ventana.after(0, actualizar_titulo)  # Actualizar el título al iniciar
ventana.mainloop()
