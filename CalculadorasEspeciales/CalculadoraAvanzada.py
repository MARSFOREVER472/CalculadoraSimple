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