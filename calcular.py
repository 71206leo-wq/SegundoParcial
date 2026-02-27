#Generar una ventana con un boton que al hacer click muestre etiqueta con el num1 y num2,para ingresar los valores 2 valores,
#Agregar  dos botones uno debajo de num2 que diga calcular y otro mas abajo a la derecha que diga resultado, sin tener funcionalidad por ahora

import tkinter as tk

# función suma
def sumar():
    n1 = float(num1.get())
    n2 = float(num2.get())
    resultado = n1 + n2
    lbl_resultado.config(text="Resultado: " + str(resultado))

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x300")

tk.Label(ventana, text="Num1:").grid(row=0, column=0, padx=4, pady=4)
num1 = tk.Entry(ventana)
num1.grid(row=0, column=1, padx=4, pady=4)

tk.Label(ventana, text="Num2:").grid(row=1, column=0, padx=4, pady=4)
num2 = tk.Entry(ventana)
num2.grid(row=1, column=1, padx=4, pady=4)

# Botón suma
tk.Button(ventana, text="Sumar", command=sumar).grid(row=2, column=0, padx=4, pady=4)

lbl_resultado = tk.Label(ventana, text="Resultado:")
lbl_resultado.grid(row=3, column=0, columnspan=2, padx=4, pady=4)

ventana.mainloop()