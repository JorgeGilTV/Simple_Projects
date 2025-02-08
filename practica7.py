import turtle
from turtle import *
import threading

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = jeni = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2000)
    contador = 0
    jeni.speed(2000)
    while (contador<100):
        brad.right(100)
        brad.forward(105)
        brad.right(90)
        brad.forward(105)
        brad.right(90)
        brad.forward(105)
        brad.right(90)
        brad.forward(105)
        contador = contador + 1
    contador = 0  
    brad.hideturtle()

    while (contador<100):
        jeni.left(100)
        jeni.forward(104.5)
        jeni.left(90)
        jeni.forward(104.5)
        jeni.left(90)
        jeni.forward(104.5)
        jeni.left(90)
        jeni.forward(104.5)
        contador = contador + 1
    jeni.hideturtle()
    contador = 0 
    while (contador<100):
        jeni.right(100)
        jeni.forward(105.5)
        jeni.right(90)
        jeni.forward(105.5)
        jeni.right(90)
        jeni.forward(105.5)
        jeni.right(90)
        jeni.forward(105.5)
        contador = contador + 1
    jeni.hideturtle()
	

