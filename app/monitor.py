import tkinter as tk
from tkinter import ttk
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MonitorRecursos:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Recursos")

        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label_cpu = tk.Label(root, text="Uso de CPU: ")
        self.label_cpu.pack()

        self.label_memoria = tk.Label(root, text="Uso de Memoria: ")
        self.label_memoria.pack()

        self.actualizar_recursos()

    def actualizar_recursos(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memoria_percent = psutil.virtual_memory().percent

        self.label_cpu.config(text=f"Uso de CPU: {cpu_percent}%")
        self.label_memoria.config(text=f"Uso de Memoria: {memoria_percent}%")

        # Actualizar el gráfico
        self.ax.clear()
        self.ax.bar(["CPU", "Memoria"], [cpu_percent, memoria_percent], color=['#FF9999', '#66B2FF'])
        self.ax.set_ylim(0, 100)
        self.ax.set_ylabel("Porcentaje")
        self.ax.set_title("Uso de Recursos")

        self.canvas.draw()

        # Programar la actualización cada segundo (1000 milisegundos)
        self.root.after(1000, self.actualizar_recursos)

root = tk.Tk()
app = MonitorRecursos(root)
root.mainloop()