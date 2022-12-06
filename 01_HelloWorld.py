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
root.title('Venatan - Hello World!')

# Etiqueta de titulo
# * Creacion de Widget -> nombre = Widget(padre, <propiedades>)
lbl_title = Label(root, text='Label de Tkinter')

# Posicionamiento con .pack
lbl_title.pack()

# Boton de acción
btn = Button(root, text='Presiona para recibir un saludo', command=saludar)
btn.pack()

# * Ciclo para mantener el programa abierto
root.mainloop()
