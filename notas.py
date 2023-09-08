 nombre = StringVar() nombre = StringVar()



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



