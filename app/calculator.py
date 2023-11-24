import tkinter as tk
from tkinter import ttk

def click_boton(caracter):
    entrada_actual = entrada.get()
    entrada.set(entrada_actual + str(caracter))

def borrar():
    entrada.set("")

def calcular():
    try:
        entrada_actual = entrada.get()
        resultado = str(eval(entrada_actual))
        entrada.set(resultado)
    except Exception as e:
        entrada.set("Error")

# Crear la ventana de la calculadora
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear la variable de control para la entrada
entrada = tk.StringVar()
entrada.set("")

# Crear la caja de entrada con estilo
caja_entrada = tk.Entry(ventana, textvariable=entrada, font=("Helvetica", 20), justify="right")
caja_entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Crear el frame de botones
frame_botones = ttk.Frame(ventana)
frame_botones.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Estilo para los botones
estilo_botones = ttk.Style()
estilo_botones.configure("TButton", padding=10, font=("Helvetica", 16,), background="#71c55b", foreground="white")

# Crear los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '', '+'
]

fila, column = 1, 0

for boton in botones:
    ttk.Button(frame_botones, text=boton, command=lambda b=boton: click_boton(b)).grid(row=fila, column=column, sticky="nsew")
    column += 1
    if column > 3:
        column = 0
        fila += 1

# Botón de borrar
ttk.Button(frame_botones, text="C", command=borrar).grid(row=fila, column=0, sticky="nsew")

# Botón de calcular
ttk.Button(frame_botones, text="=", command=calcular).grid(row=fila, column=1, columnspan=2, sticky="nsew")

# Configurar el diseño de la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Iniciar la aplicación
ventana.mainloop()