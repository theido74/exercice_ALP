from turtle import *

dim = int(input('Entrez la dimension : '))
def turnleft90():
    left(90)
def rowanddot(dim):
    forward(dim)
    dot(20)
    backward(dim)
    dot(10)

def draw_cross():
    for _ in range(4):
        rowanddot(dim)
        turnleft90()
    done()

draw_cross()

