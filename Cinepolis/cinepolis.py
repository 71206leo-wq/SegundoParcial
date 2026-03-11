import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


# ----------- FUNCION PROCESAR -----------
def procesar():

    try:
        nombre_cliente = nombre.get()
        personas = int(compradores.get())
        boletos = int(cant_boletos.get())

        max_boletos = personas * 7

        if boletos > max_boletos:
            messagebox.showerror("Error", f"Solo puedes comprar hasta {max_boletos} boletos")
            return

        precio = 12
        total = boletos * precio

        # DESCUENTOS POR CANTIDAD
        if boletos > 5:
            total = total * 0.85
        elif boletos >= 3:
            total = total * 0.90

        # DESCUENTO TARJETA
        if tarjeta.get() == "si":
            total = total * 0.90

        resultado.delete(0, tk.END)
        resultado.insert(0, round(total,2))

    except:
        messagebox.showerror("Error", "Ingresa datos válidos")

# ----------- VENTANA PRINCIPAL -----------
ventana = tk.Tk()
ventana.title("Cinépolis")
ventana.geometry("500x320")
ventana.config(bg="royalblue")

titulo = tk.Label(ventana,text="CINÉPOLIS",font=("Arial",16,"bold"),bg="royalblue",fg="white")
titulo.grid(row=0,column=0,columnspan=2,pady=10)

# ----------- ENTRADAS -----------
frame1 = tk.LabelFrame(ventana,text="Entradas",bg="royalblue",fg="white")
frame1.grid(row=1,column=0,padx=20,pady=10)

tk.Label(frame1,text="Nombre",bg="royalblue",fg="white").grid(row=0,column=0)
nombre = tk.Entry(frame1)
nombre.grid(row=0,column=1)

tk.Label(frame1,text="Cantidad Compradores",bg="royalblue",fg="white").grid(row=1,column=0)
compradores = tk.Entry(frame1)
compradores.grid(row=1,column=1)

tk.Label(frame1,text="Tarjeta CINECO",bg="royalblue",fg="white").grid(row=2,column=0)

tarjeta = tk.StringVar()

tk.Radiobutton(frame1,text="Si",variable=tarjeta,value="si",bg="royalblue").grid(row=2,column=1,sticky="w")
tk.Radiobutton(frame1,text="No",variable=tarjeta,value="no",bg="royalblue").grid(row=2,column=1,sticky="e")

tk.Label(frame1,text="Cantidad de Boletos",bg="royalblue",fg="white").grid(row=3,column=0)
cant_boletos = tk.Entry(frame1)
cant_boletos.grid(row=3,column=1)

# ----------- SALIDAS -----------
frame2 = tk.LabelFrame(ventana,text="Salidas",bg="royalblue",fg="white")
frame2.grid(row=1,column=1,padx=20)

tk.Label(frame2,text="Valor a pagar",bg="royalblue",fg="white").grid(row=0,column=0)
resultado = tk.Entry(frame2)
resultado.grid(row=0,column=1)

# ----------- BOTONES -----------
frame3 = tk.Frame(ventana,bg="royalblue")
frame3.grid(row=2,column=0,columnspan=2,pady=20)

tk.Button(frame3,text="Procesar",command=procesar).grid(row=0,column=0,padx=10)
tk.Button(frame3,text="Salir",command=ventana.quit).grid(row=0,column=1,padx=10)

ventana.mainloop()
