# Importaciones
from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo

# Evento del boton


def saludar():
    showinfo(
        title='Saludo',
        message='Hola Mundo!'
    )


# Ventana raiz
root = Tk()

# Tamaño de la ventana
root.geometry('400x280')


# Titulo de la ventana
root.title('Ventana - Hello World!')

# Configurar ventana
root.config(bg="#22272e")

# Etiqueta de titulo
# * Creacion de Widget -> nombre = Widget(padre, <propiedades>)
lbl_title = Label(root, text='Primer programa Tkinter')

# Configurar label
lbl_title.config(bg="#22272e", fg="#a9b2bf")

# Posicionamiento con .pack
lbl_title.pack()

# Boton de acción
btn = Button(root, text='Presiona para recibir un saludo', command=saludar)
btn.pack()

# * Ciclo para mantener el programa abierto
root.mainloop()
