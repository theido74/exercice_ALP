from turtle import *

def draw_figure(cotes,perimetre):
    if cotes == 3:
        perimetre = perimetre / 3
        for _ in range(3):
            forward(perimetre)
            left(120)
    elif cotes == 4:
        perimetre = perimetre / 4
        for _ in range(4):
            forward(perimetre)
            left(90)
    elif cotes == 5:
        perimetre = perimetre / 5
        for _ in range(5):
            forward(perimetre)
            left(72)
    else:
        print('Je ne sais rien faire d\'autres')

draw_figure(5,200)

        