import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


#instalar  pip install pillow
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Cerrar con confirmacion")
root.geometry("400x300")
def cerrar():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres cerrar la ventana?")
    if respuesta:
        root.destroy()

#Cargar la imagen
imagen = Image.open("Fondo.jpg")
fondo = ImageTk.PhotoImage(imagen)

#label como fondo
label_fondo = tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
frame_acciones = tk.LabelFrame(root, text="Acciones", bg="#1E3A8A", fg="white", padx=10, pady=10) 
frame_acciones.place(x=200, y=250, width=200, height=100)

tk.Button(frame_acciones, text="Salir", command=cerrar).pack(pady=20)

root.mainloop()

