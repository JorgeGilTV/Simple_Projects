from tkinter import *
import tkinter as tk


class SumaOption:

    def __init__(self, top):
        self.top = top
        self.monitor = Label(self.top)
        self.e1 = Entry(self.top)
        self.e2 = Entry(self.top)
        
    def sumar(self):
        suma = int(self.e1.get())+int(self.e2.get())
        self.resultado = str(self.e1.get())+"+"+str(self.e2.get())+"="+str(suma)
        self.monitor.config(text="{}".format(suma))

    def validate_input(self,input):
        if input.isdigit():
            return True
        else:
            return False
        
    def inicia(self):
        self.top.title("Suma de dos enteros")
        validate = self.top.register(self.validate_input)

        l1 =Label(self.top, text="Indica el primer número")
        l1.pack()
        self.e1 = Entry(self.top, validate="key", validatecommand=(validate, "%P"))
        self.e1.pack()
        l2 = Label(self.top, text="Indica el Segundo número")
        l2.pack()
        self.e2 = Entry(self.top, validate="key",validatecommand=(validate, "%P"))
        self.e2.pack()
        sumButton = Button(self.top, text="Submit", width=10, command= self.sumar)
        sumButton.pack()
        self.monitor.pack()
        self.top.mainloop()


