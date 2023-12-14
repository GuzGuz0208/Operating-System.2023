import os
import tkinter as tk
from tkinter import filedialog
import pygame

class ReproductorAudio:
    def __init__(self, master):
        self.master = master
        master.title("Reproductor de Audio")
        
        self.playlist = []
        self.current_index = 0

        # Inicializar Pygame
        pygame.init()

        # Crear widgets
        self.label = tk.Label(master, text="Reproductor de Audio")
        self.label.pack()

        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.listbox.pack()

        self.btn_add = tk.Button(master, text="Agregar Canciones", command=self.agregar_canciones)
        self.btn_add.pack()

        self.btn_play = tk.Button(master, text="Reproducir", command=self.reproducir)
        self.btn_play.pack()

        self.btn_pause = tk.Button(master, text="Pausar", command=self.pausar)
        self.btn_pause.pack()

        self.btn_stop = tk.Button(master, text="Detener", command=self.detener)
        self.btn_stop.pack()

        self.btn_siguiente = tk.Button(master, text="Siguiente", command=self.siguiente_cancion)
        self.btn_siguiente.pack()

    def agregar_canciones(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Archivos de audio", "*.mp3;*.wav")])
        if file_paths:
            self.playlist.extend(file_paths)
            for file_path in file_paths:
                self.listbox.insert(tk.END, os.path.basename(file_path))

    def reproducir(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pausar(self):
        pygame.mixer.music.pause()

    def detener(self):
        pygame.mixer.music.stop()

    def siguiente_cancion(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.reproducir()

if __name__ == "__main__":
    root = tk.Tk()
    reproductor = ReproductorAudio(root)
    root.mainloop()