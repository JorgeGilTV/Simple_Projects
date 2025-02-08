from tkinter import *
import tkinter as tk
import math

class HexadecimalConvertor:

    def __init__(self, top):
        self.top = top
        self.monitor = Label(self.top)
        self.e1 = Entry(self.top)

    
    def calcular(self):
        numeroBinarioStr = ""
        numeroEntero = int(self.e1.get())
        while(numeroEntero // 2 != 0):
            residuo = numeroEntero % 2
            numeroBinarioStr  = str(residuo) + numeroBinarioStr
            numeroEntero = numeroEntero // 2
            if numeroEntero < 2:
                numeroBinarioStr = str(numeroEntero) + numeroBinarioStr
        if len(numeroBinarioStr) < 8:
            while(len(numeroBinarioStr)  < 8):
                numeroBinarioStr = "0"+numeroBinarioStr
            
        self.monitor.config(text="{}".format(numeroBinarioStr))

    def validate_input(self,input):
        if input.isdigit():
            return True
        else:
            return False
        
    def inicia(self):
        self.top.title("Convertidor a Binario")
        validate = self.top.register(self.validate_input)

        l1 =Label(self.top, text="Indica el numero entero que quieres convertir")
        l1.pack()
        self.e1 = Entry(self.top, validate="key", validatecommand=(validate, "%P"))
        self.e1.pack()

        sumButton = Button(self.top, text="Submit", width=10, command= self.calcular)
        sumButton.pack()
        self.monitor.pack()
        self.top.mainloop()
