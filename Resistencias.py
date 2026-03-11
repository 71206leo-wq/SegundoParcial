import tkinter as tk

# Diccionario de colores y valores
colores = {
    "Negro": 0,
    "Cafe": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Gris": 8,
    "Blanco": 9
}

# Función para calcular resistencia
def calcular():
    c1 = colores[color1.get()]
    c2 = colores[color2.get()]
    c3 = colores[color3.get()]

    valor = (c1 * 10 + c2) * (10 ** c3)

    if tolerancia.get() == "oro":
        tol = 0.05
    else:
        tol = 0.10

    maximo = valor + valor * tol
    minimo = valor - valor * tol

    resultado_ohm.config(text=str(valor))
    resultado_max.config(text=str(round(maximo,2)))
    resultado_min.config(text=str(round(minimo,2)))


ventana = tk.Tk()
ventana.title("Calculadora de Resistencias")

# Variables
color1 = tk.StringVar(value="Negro")
color2 = tk.StringVar(value="Negro")
color3 = tk.StringVar(value="Negro")
tolerancia = tk.StringVar(value="oro")

# Título
tk.Label(ventana, text="Calcular Valor de Resistencias", font=("Arial",12)).grid(row=0,column=0,columnspan=2)

# Listas desplegables
tk.Label(ventana,text="Primer color").grid(row=1,column=0)
tk.OptionMenu(ventana,color1,*colores.keys()).grid(row=1,column=1)

tk.Label(ventana,text="Segundo color").grid(row=2,column=0)
tk.OptionMenu(ventana,color2,*colores.keys()).grid(row=2,column=1)

tk.Label(ventana,text="Multiplicador").grid(row=3,column=0)
tk.OptionMenu(ventana,color3,*colores.keys()).grid(row=3,column=1)

# Radio botones tolerancia
tk.Label(ventana,text="Tolerancia").grid(row=4,column=0)

tk.Radiobutton(ventana,text="Oro (5%)",variable=tolerancia,value="oro").grid(row=4,column=1)
tk.Radiobutton(ventana,text="Plata (10%)",variable=tolerancia,value="plata").grid(row=5,column=1)

# Botón calcular
tk.Button(ventana,text="Calcular",command=calcular).grid(row=6,column=0,columnspan=2)

# Resultados
tk.Label(ventana,text="Valor Ohm:").grid(row=7,column=0)
resultado_ohm = tk.Label(ventana,text="0")
resultado_ohm.grid(row=7,column=1)

tk.Label(ventana,text="Valor Máximo:").grid(row=8,column=0)
resultado_max = tk.Label(ventana,text="0")
resultado_max.grid(row=8,column=1)

tk.Label(ventana,text="Valor Mínimo:").grid(row=9,column=0)
resultado_min = tk.Label(ventana,text="0")
resultado_min.grid(row=9,column=1)

ventana.mainloop()
