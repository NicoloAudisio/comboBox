# Audisio Combobox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Finestra(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audisio Combobox")
        self.geometry("500x500")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        opzioni = ["opzione 1", "opzione 2", "opzione 3"]

        self.combo = ttk.Combobox(self, values=opzioni)
        self.combo.pack()

        self.button = tk.Button(self, text="Scelta", command=self.visualizza_selezione)
        self.button.pack()

    def visualizza_selezione(self):
        selezione = self.combo.get()
        tk.messagebox.showinfo("Selezione", "Hai selezionato: {}".format(selezione))

root = Finestra()
root.mainloop()