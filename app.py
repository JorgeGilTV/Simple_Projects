from flask import Flask, render_template, url_for, request, redirect
import practica1
import practica2
import practica3
import practica4
import practica5
import practica6
import practica7
#import menuc
from tkinter import *

app = Flask(__name__)
variableToDisplay = ''


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/callPractice/<int:no_practice>')
def callPractice(no_practice):
    if no_practice == 1:
       top = Tk()
       variableToDisplay =  practica1.begin(top)
       
    elif no_practice == 2:
        top = Tk()
        p2 = practica2.SumaOption(top)
        p2.inicia()
    elif no_practice == 3:
        top = Tk()
        p3 = practica3.VolumenOption(top)
        p3.inicia()
    elif no_practice == 4:
        top = Tk()
        p4 = practica4.BooleanOption(top)
        p4.inicia()
    elif no_practice == 5:
        top = Tk()
        p5 = practica5.HexadecimalConvertor(top)
        p5.inicia()
    elif no_practice == 6:
        top = Tk()
        p6 = practica6.HexadecimalConvertor(top)
        p6.inicia()         
    elif no_practice == 7:
        practica7.draw_square()
    elif no_practice == 8:
        top = Tk()
        p8 = menuc.HexadecimalConvertor(top)
        p8.inicia()         
    else:
        print('nada que hacer')
        
    return render_template('index.html')
    





    
if __name__ == "__main__":
    app.run(debug = True)
