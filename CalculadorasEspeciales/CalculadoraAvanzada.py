import math
import tkinter as tk
from tkinter import messagebox

class CalculadoraAvanzada:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora Avanzada")
        self.raiz.geometry("380x520")
        self.raiz.config(bg="#2B2B2B")
        self.raiz.resizable(False, False)

        self.expresion = ""
        self.entrada_texto = tk.StringVar()

        # PANTALLA DE VISUALIZACIÓN:

        self.crear_pantalla()

        # BOTONES DE LA CALCULADORA:

        self.crear_botones()

        def crear_pantalla(self):
            pantalla_frame = tk.Frame(self.raiz, width=380, height=80, bg="#2B2B2B")
            pantalla_frame.pack(pack_propagate=False, fill="both")

            anadir_pantalla= tk.Entry(pantalla_frame, textvariable=self.entrada_texto, font=("Arial", 22), bg="#1C1C1C", fg="#FFFFFF", bd=0, justify="right")
            anadir_pantalla.pack(expand=True, fill="both", padx=10, pady=10)