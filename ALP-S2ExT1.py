from turtle import *
def i_grec():
    left(30)
    forward(20)

    backward(20)
    right(60)
    forward(20)

def double_i_grec():
    i_grec()
    i_grec()
    
def branche():
    left(90)
    forward(40)


branche()
tp = pos()
print(tp)
left(30)
forward(20)
tp_gauche = pos()
print(tp_gauche)
i_grec()
i_grec()
teleport(tp_gauche[0], tp_gauche[1])
left(90)
forward(20)
i_grec()
teleport(tp[0],tp[1])
right(60)
forward(20)
tp_droite = pos()
left(30)
forward(20)
i_grec()
teleport(tp_droite[0], tp_droite[1])
double_i_grec()

done()
