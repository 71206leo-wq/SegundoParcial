import tkinter as tk

def deshabilitar():
    radio1.config(state="disabled")

def habilitar():
    radio1.config(state="normal")

ventana = tk.Tk()
ventana.title("Radios Habilitar/Deshabilitar")
ventana.geometry("300x200")

opcion= tk.IntVar()

radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value=1)
radio1.pack(pady=10)

tk.Button(ventana, text="Deshabilitar Opción 1", command=deshabilitar).pack(pady=5)
tk.Button(ventana, text="Habilitar Opción 1", command=habilitar).pack(pady=5)

ventana.mainloop()