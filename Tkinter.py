from tkinter import *
import os

def get_calc():
    os.system("calc")

ventana = Tk()
ventana.title("Primera Ventana")
ventana.geometry("520x480")
ventana.config(bg="#45ad87")
ventana.resizable(0,0)
boton = Button(text = "Abrir calculadora", comnand=None)
boton.place(x=100,y=50)
ventana.mainloop()
