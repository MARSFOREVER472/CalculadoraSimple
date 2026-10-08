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
            entrada.pack(padx=20, pady=20, ipady=10, fill="both")

        def click_boton(self, valor):
            self.ecuacion += str(valor)
            self.entrada_texto.set(self.ecuacion)

        def limpiar(self):
            self.ecuacion = ""
            self.pantalla_texto.set("")

        def calcular(self):
            try:
                # REEMPLAZOS VISUALES PARA EVALUAR LA EXPRESIÓN DE FORMA SEGURA O DIRECTAMENTE USAR eval() SI SE CONFÍA EN LA ENTRADA DEL USUARIO...

                expresion = (self.ecuacion.replace("×", "*").replace("÷", "/").replace("^", "**"))

                # FUNCIONES CIENTÍFICAS COMUNES USANDO LA FUNCIÓN "math"...

                expresion = expresion.replace("sin(", "math.sin(math.radians(").replace("cos(", "math.cos(math.radians(").replace("tan(", "math.tan(math.radians(").replace("sqrt(", "math.sqrt(")

                # SI ABRIMOS RADIANES CON FUNCIONES TRIGONOMÉTRICAS, AJUSTAMOS PARÉNTESIS EXTRA SI ES NECESARIO...
                # PARA SIMPLIFICAR EL eval BÁSICO CON FUNCIONES DE math:

                resultado = eval(expresion)
                self.pantalla_texto.set(str(resultado))
                self.ecuacion = str(resultado)
            except Exception:
                messagebox.showerror("Error", "Operación no válida")
                self.limpiar()

            def crear_botones(self):

                botones = [
                    ("C", 0, 0),
                    ("(", 0, 1),
                    (")", 0, 2),
                    ("÷", 0, 3),
                    ("sin", 1, 0),
                    ("cos", 1, 1),
                    ("tan", 1, 2),
        ("×", 1, 3),
        ("7", 2, 0),
        ("8", 2, 1),
        ("9", 2, 2),
        ("-", 2, 3),
        ("4", 3, 0),
        ("5", 3, 1),
        ("6", 3, 2),
        ("+", 3, 3),
        ("1", 4, 0),
        ("2", 4, 1),
        ("3", 4, 2),
        ("=", 4, 3),
        ("0", 5, 0),
        (".", 5, 1),
        ("sqrt", 5, 2),
        ("^", 5, 3), 

        for texto, fila, col in botones:
                if texto == "=":
                    cmd = self.calcular
                    bg_color = "#ff9800"
                elif texto == "C":
                    cmd = self.limpiar
                    bg_color = "#f44336"
                else:
                    cmd = lambda t = texto: self.click_boton(
                        t + ("(" if t in ["sin", "cos", "tan", "sqrt"] else "")
                    )
                    bg_color = "#444444"
        
                    b = tk.Button(marco_botones, text = texto, font = ("Arial", 14), bg = bg_color, fg = "#FFFFFF", bd = 0, command = cmd)
                    b.grid(row = fila, column = col, sticky = "nsew", padx = 3, pady = 3)  
    ]
