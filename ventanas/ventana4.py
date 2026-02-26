import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    texto = entrada.get()
    label_resultado.config(text=f"Escribiste: {texto}")

ventana = tk.Tk()
ventana.title("Ejemplo con Entry")
ventana.geometry("400x300")

#creamos entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=20)

#boton moderno
boton_mostrar = ttk.Button(ventana, text="Enviar", command=mostrar_texto)
boton_mostrar.pack(pady=10)

label_resultado = ttk.Label(ventana, text="")
label_resultado.pack(pady=20)

ventana.mainloop()
    