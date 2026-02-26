import tkinter as tk

#creamos ventana principal
def saludo():
    label_resultado.config(text="Hola alumnos de python")
ventana = tk.Tk()
#le damos un titulo a la ventana
ventana.title("Mi primera aplicacion")
#le damos un tamaño a la ventana
ventana.geometry("400x300")

#creamos un boton
boton_saludo = tk.Button(ventana, text="Saludar", command=saludo)
boton_saludo.pack(pady=20)



#creamos una etiqueta
label_resultado = tk.Label(ventana, text="", 
                    font=("Arial", 16, "bold"))

#mostramos la etiqueta en la ventana
label_resultado.pack(pady=20)
ventana.mainloop()
