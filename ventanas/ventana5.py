import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("400x300")

# Crear etiquetas y entradas para los números
tk.Label(ventana, text="Primer numero:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo numero:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Crear botón de suma
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)

# Crear etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

ventana.mainloop()
