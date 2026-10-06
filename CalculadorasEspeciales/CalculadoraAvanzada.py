import math
import tkinter as tk
from tkinter import messagebox

class CalculadoraAvanzada:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada")
        self.root.geometry("400x550")
        self.root.config(bg="#222222")
        self.root.resizable(False, False)

        self.ecuacion = ""
        self.entrada_texto = tk.StringVar()

        # PANTALLA DE VISUALIZACIÓN:

        self.crear_pantalla()

        # BOTONES DE LA CALCULADORA:

        self.crear_botones()

        def crear_pantalla(self):

            entrada= tk.Entry(self.root, textvariable=self.entrada_texto, font=("Arial", 22), bg="#333333", fg="#FFFFFF", bd=0, justify="right")
            entrada.pack(padx=20, pady=20, ippady=10, fill="both")