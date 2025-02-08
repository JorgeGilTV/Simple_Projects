from tkinter import *
import tkinter as tk
import math

class HexadecimalConvertor:

    def __init__(self, top):
        self.top = top
        self.monitor = Label(self.top)
        self.e1 = Entry(self.top)

    
    def calcular(self):
        numeroHexadecimanlStr = ""
        hexaValues = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        numeroEntero = int(self.e1.get())
        while(numeroEntero % 16 != 0):
            residuo = numeroEntero % 16
            if residuo > 9:
                numeroHexadecimanlStr = hexaValues.get(residuo) + numeroHexadecimanlStr
            else:       
                numeroHexadecimanlStr  = str(residuo) + numeroHexadecimanlStr
            numeroEntero = numeroEntero // 16
        if(numeroEntero >0):
            numeroHexadecimanlStr =str(numeroEntero) + numeroHexadecimanlStr
            
        self.monitor.config(text="{}".format(numeroHexadecimanlStr))

    def validate_input(self,input):
        if input.isdigit():
            return True
        else:
            return False
        
    def inicia(self):
        self.top.title("Convertidor a Hexadecimal")
        validate = self.top.register(self.validate_input)

        l1 =Label(self.top, text="Indica el numero entero que quieres convertir")
        l1.pack()
        self.e1 = Entry(self.top, validate="key", validatecommand=(validate, "%P"))
        self.e1.pack()

        sumButton = Button(self.top, text="Submit", width=10, command= self.calcular)
        sumButton.pack()
        self.monitor.pack()
        self.top.mainloop()
