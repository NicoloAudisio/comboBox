# Audisio esempio utilizzo Combobox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Finestra(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prenotazione Hotel")
        self.geometry("700x500")
        self.resizable(0, 0)
    
    # --- FUNZIONI ---
    def prenota(self):
        try:
            with open("prenotazioni.txt", "a") as f:
                servizi = []
                if self.piscina.get() == True:
                    servizi.append("Piscina")
                if self.parcheggio.get():
                    servizi.append("Parcheggio")
                if self.wifi.get():
                    servizi.append("Wi-Fi")
                servizi_str = ",".join(servizi) # unisce tutte le stringhe, inserendo la ","
                prenotazione = f"Ripilogo prenotazione\nIl sig. {self.cognome_entry.get()} {self.nome_entry.get()} ha prenotato una stanza {self.tipologia_camera.get()} per {self.notti.get()} notti\nServizi richiesti: {servizi_str}\nTipologia pensione: {self.combo.get()}\n"
                f.write(prenotazione)
                self.lbl_conferma.config(text = "Prenotazione effettuata con successo!")
                self.lbl_conferma.config(fg = 'green')
        except ValueError:
            messagebox.showerror("Errore", "Errore nell'inserimento dei dati")


    def crea_widgets(self):
        # --- LABEL HOTEL BELLAVISTA
        lbl_hotel = tk.Label(self, text="Hotel Rimini", font=("Time New Romans", 20))
        lbl_hotel.pack(pady=20)

        # --- COGNOME E NOME---
        frm_dati = tk.Frame(self)
        lbl_cognome = tk.Label(frm_dati, text="Cognome")
        lbl_cognome.pack(side=tk.LEFT, padx=10)
        self.cognome_entry = tk.Entry(frm_dati)
        self.cognome_entry.pack(side=tk.LEFT)

        lbl_nome = tk.Label(frm_dati, text="Nome")
        lbl_nome.pack(side=tk.LEFT, padx=10)
        self.nome_entry = tk.Entry(frm_dati)
        self.nome_entry.pack(side=tk.LEFT)
        frm_dati.pack(pady=10)

        # --- SCELTA CAMERA ---
        lbl_camera = tk.Label(self, text="Tipologia camera: ")
        lbl_camera.pack()
        self.tipologia_camera = tk.StringVar()
        self.tipologia_camera.set("Singola")
        rbt_singola = tk.Radiobutton(self, text="Singola", variable=self.tipologia_camera, value="Singola")
        rbt_singola.pack()
        rbt_matrimoniale = tk.Radiobutton(self, text="Matrimoniale", variable=self.tipologia_camera, value="Matrimoniale")
        rbt_matrimoniale.pack()

        # --- NUMERO NOTTI ---
        lbl_notti = tk.Label(self, text="Numero notti")
        lbl_notti.pack()
        self.notti = tk.StringVar()
        self.notti.set("1")
        spin_notti = tk.Spinbox(self, from_=1, to=30, textvariable=self.notti)
        spin_notti.pack()

        # --- SCLETA PENSIONE ---
        lbl_piano = tk.Label(self, text="Tipologia di pensione")
        lbl_piano.pack()
        opzioni = ["Solo colazione", "Mezza pensione", "Pensione completa"]
        self.combo = ttk.Combobox(self, values=opzioni)
        self.combo.pack()

        # --- SERVIZI EXTRA ---
        lbl_serviziExtra = tk.Label(self, text="Servizi extra")
        lbl_serviziExtra.pack()
        self.piscina = tk.BooleanVar()
        chk_piscina = tk.Checkbutton(self, text="Piscina", variable=self.piscina)
        chk_piscina.pack()
        self.parcheggio = tk.BooleanVar()
        chk_parcheggio = tk.Checkbutton(self, text="Parcheggio", variable=self.parcheggio)
        chk_parcheggio.pack()
        self.wifi = tk.BooleanVar()
        chk_wifi = tk.Checkbutton(self, text="Wi-Fi", variable=self.wifi)
        chk_wifi.pack()

        # --- BOTTONE PRENOTA ---
        btn_prenota = tk.Button(self, text="Prenota", command=self.prenota)
        btn_prenota.pack(pady=20)

        # --- LABLE CONFERMA ---
        self.lbl_conferma = tk.Label(self, text="")
        self.lbl_conferma.pack()

root = Finestra()
root.crea_widgets()
root.mainloop()