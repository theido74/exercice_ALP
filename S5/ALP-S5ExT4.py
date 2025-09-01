from turtle import *

def depart():
    teleport(-400,0)
    left(45)
    
def triangle():
    dot(10)
    fd(120)
    dot(10)
    right(90)
    fd(120)
    left(90)

showturtle()
depart()
for _ in range(4):
     triangle()
