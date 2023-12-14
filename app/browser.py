import tkinter as tk
from tkinter import ttk
import webbrowser

class NavegadorWeb(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Navegador Web Básico")
        self.geometry("800x600")

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack(fill=tk.X, padx=10, pady=10)

        self.navegar_button = ttk.Button(self, text="Ir", command=self.ir_a_url)
        self.navegar_button.pack(pady=5)

        self.web_browser = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        self.web_browser.pack(padx=10, pady=10)

    def ir_a_url(self):
        url = self.url_entry.get()
        if url.startswith(('http://', 'https://')):
            self.web_browser.delete(1.0, tk.END)
            webbrowser.open_new(url)
        else:
            self.web_browser.delete(1.0, tk.END)
            self.web_browser.insert(tk.END, "Ingrese una URL válida (con http:// o https://)")

if __name__ == "__main__":
    app = NavegadorWeb()
    app.mainloop()