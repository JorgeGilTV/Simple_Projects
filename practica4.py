from tkinter import *
import tkinter as tk   

class BooleanOption:
    def __init__(self, top):
        self.top = top
        self.monitor = Label(self.top)
        self.opcion = IntVar()
        
    def createText(option):
        text = ''
        if option == 1:
            text = "Verdadero es igual a 1"
        else:
            text = "Falso es igual a 0"
        return text

    def selection(self):
        self.monitor.config(text="{}".format(self.opcion.get()))
  

    def inicia(self):
        self.top.title("Convertir las palabras Verdadero y Falso a 1 y 0, respectivamente")
        self.top.geometry("300x100")
        self.opcion = IntVar()
        Radiobutton(self.top, text="VERDADERO", variable=self.opcion,value=1, command=self.selection).pack()
        Radiobutton(self.top, text="FALSO", variable=self.opcion,value=0, command=self.selection).pack()
        self.monitor.pack() 
        self.top.mainloop()
