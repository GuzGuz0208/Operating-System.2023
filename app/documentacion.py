import tkinter as tk

def abrir_aplicacion(nombre):
    ventana_app = tk.Toplevel()
    ventana_app.title(nombre)
    ventana_app.geometry("800x600")
# Crear la ventana principal del escritorio
ventana = tk.Tk()

def info():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Información")
    nueva_ventana.geometry("500x300")

    label = tk.Label(nueva_ventana, text="Información del Sistema", font=("Helvetica", 16))
    label.pack(pady=20)

    # Información detallada
    info_text = (
        "Sistema operativo: LuckyOS \n"
        "Propietario(a): Juan Esteban Guzmán Henao\n"
        "Lenguaje: Python, Tkinter\n"
        "Bibliografía:\n"
        "  - https://stackoverflow.com/\n"
        "  - https://chat.openai.com/"
    )

    info_label = tk.Label(nueva_ventana, text=info_text, justify=tk.LEFT)
    info_label.pack(pady=20)

# Llamas a la función para abrir la ventana de información
info()
#Quiero que se ejecute
ventana.mainloop()