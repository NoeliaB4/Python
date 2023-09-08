from tkinter import *
from tkinter import messagebox
from BIBLIOTECA.Biblioteca import Biblioteca

biblioteca = None 

def crear_biblio():
    nombre = StringVar()
    def guardar_nombre():
        biblioteca = Biblioteca(nombre.get())
        messagebox.showinfo(message="Se ha creado la biblioteca", title="Mensaje")
        v_biblio.destroy()

    v_biblio = Toplevel(ventana)
    v_biblio.title("Gestionar biblioteca")
    v_biblio.geometry("400x200+350+150")
    lbl_nombre = Label(v_biblio,text="Ingrese nombre:" )
    lbl_nombre.place(x=5,y =10 )
    t_nombre = Entry(v_biblio,textvariable=nombre)
    t_nombre.place(x = 100, y =10)
    b_guardar = Button(v_biblio,text="Guardar", command=guardar_nombre)
    b_guardar.place(x=300, y = 10)


def agregar_libro():
    pass

ventana = Tk()
ventana.geometry("640x480+300+200")
ventana.title("SISTEMA BIBLIOTECARIO")
ventana.config(bg = "#94AFCC")

boton_crear_biblioteca = Button(ventana,text="Crear biblioteca", command=crear_biblio)
boton_crear_biblioteca.place(x=50, y= 50)
boton_agregar_libro = Button(ventana, text="Agregar libro", command=agregar_libro)
boton_agregar_libro.place(x=50, y = 100)
ventana.mainloop()