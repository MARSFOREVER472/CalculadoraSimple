import math
import tkinter as tk
from tkinter import messagebox


class CalculadoraAvanzada:

  def __init__(self, root):
    self.root = root
    self.root.title("Calculadora Avanzada Python")
    self.root.geometry("350x500")
    self.root.resizable(False, False)

    self.expresion = ""
    self.pantalla_texto = tk.StringVar()

    # Campo de pantalla
    input_frame = tk.Frame(self.root, width=350, height=80, bg="gray20")
    input_frame.pack(side=tk.TOP)

    input_field = tk.Entry(
        input_frame,
        font=("arial", 20, "bold"),
        textvariable=self.pantalla_texto,
        bg="gray85",
        fg="black",
        bd=10,
        insertwidth=4,
        width=20,
        justify="right",
    )
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=20)

    # Botonera
    btn_frame = tk.Frame(self.root, width=350, height=420, bg="gray")
    btn_frame.pack()

    # Botones
    botones = [
        ("C", 1, 0),
        ("(", 1, 1),
        (")", 1, 2),
        ("/", 1, 3),
        ("sin", 2, 0),
        ("cos", 2, 1),
        ("tan", 2, 2),
        ("*", 2, 3),
        ("7", 3, 0),
        ("8", 3, 1),
        ("9", 3, 2),
        ("-", 3, 3),
        ("4", 4, 0),
        ("5", 4, 1),
        ("6", 4, 2),
        ("+", 4, 3),
        ("1", 5, 0),
        ("2", 5, 1),
        ("3", 5, 2),
        ("√", 5, 3),
        ("0", 6, 0),
        (".", 6, 1),
        ("**", 6, 2),
        ("=", 6, 3),
    ]

    for texto, fila, col in botones:
      btn = tk.Button(
          btn_frame,
          text=texto,
          fg="black",
          width=7,
          height=3,
          bd=1,
          bg="white",
          command=lambda t=texto: self.clic_boton(t),
      )
      btn.grid(row=fila, column=col)

  def clic_boton(self, char):
    if char == "C":
      self.expresion = ""
      self.pantalla_texto.set("")
    elif char == "=":
      try:
        # Reemplazar símbolos para que Python los entienda
        exp_eval = self.expresion.replace("√", "math.sqrt")
        resultado = str(eval(exp_eval))
        self.pantalla_texto.set(resultado)
        self.expresion = resultado
      except Exception:
        messagebox.showerror("Error", "Operación no válida")
        self.expresion = ""
        self.pantalla_texto.set("")
    elif char in ["sin", "cos", "tan"]:
      try:
        val = float(self.expresion)
        if char == "sin":
          res = math.sin(math.radians(val))
        elif char == "cos":
          res = math.cos(math.radians(val))
        elif char == "tan":
          res = math.tan(math.radians(val))
        self.pantalla_texto.set(str(res))
        self.expresion = str(res)
      except Exception:
        messagebox.showerror("Error", "Valor inválido para función trigonométrica")
    else:
      self.expresion += str(char)
      self.pantalla_texto.set(self.expresion)


if __name__ == "__main__":
  ventana = tk.Tk()
  app = CalculadoraAvanzada(ventana)
  ventana.mainloop()

