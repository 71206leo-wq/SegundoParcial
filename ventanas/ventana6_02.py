import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = opcion.get()

        if operacion == 1:
            resultado = num1 + num2
        elif operacion == 2:
            resultado = num1 - num2
        elif operacion == 3:
            resultado = num1 * num2
        elif operacion == 4:
            if num2 == 0:
                messagebox.showwarning("Advertencia", "No se puede dividir por cero.")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "Selecciona una operación válida.")
            return

            etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# ======================
# VENTANA PRINCIPAL
# ======================

ventana = tk.Tk()
ventana.title("Calculadora con Radiobotones")
ventana.geometry("400x300")

# Entradas
tk.Label(ventana, text="Primer numero:").grid(row=0, column=0)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1)

tk.Label(ventana, text="Segundo numero:").grid(row=1, column=0)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1)

# Radiobotones
opcion = tk.IntVar()

tk.Label(ventana, text="Selecciona una operación:").grid(row=2, column=0, columnspan=2)

tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).grid(row=3, column=0)
tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).grid(row=3, column=1)
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).grid(row=4, column=0)
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).grid(row=4, column=1)

# Botón
tk.Button(ventana, text="Calcular", command=calcular).grid(row=5, column=0, columnspan=2)