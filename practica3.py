from tkinter import *
import tkinter as tk
import math

class VolumenOption:

    def __init__(self, top):
        self.top = top
        self.monitor = Label(self.top)
        self.e1 = Entry(self.top)

    
    def calcular(self):
        volumen = ((4/3) * math.pi)* int(self.e1.get())**3
        self.resultado = str(self.e1.get())+"+"+str(self.e1.get())+"="+str(volumen)
        self.monitor.config(text="{}".format(volumen))

    def validate_input(self,input):
        if input.isdigit():
            return True
        else:
            return False
        
    def inicia(self):
        self.top.title("Calculando el volumen de una esfera")
        validate = self.top.register(self.validate_input)

        l1 =Label(self.top, text="Indica el valor del radio")
        l1.pack()
        self.e1 = Entry(self.top, validate="key", validatecommand=(validate, "%P"))
        self.e1.pack()

        sumButton = Button(self.top, text="Submit", width=10, command= self.calcular)
        sumButton.pack()
        self.monitor.pack()
        self.top.mainloop()
