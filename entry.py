from tkinter import *

top = Tk()
def inicia(top):
    L1 = Label(top, text = "User Name")
    L1.pack (side = LEFT)
    E1 = Entry(top,bd = 5)
    E1.pack(side = RIGHT)
    top.mainloop()
