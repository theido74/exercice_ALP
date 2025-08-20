from turtle import *

forme = input('Entrez la forme à dessiner (carré, ligne) :').lower()

if forme == 'carré':
    longueur = int(input('Entrez la longueur du carré : '))
    for _ in range(4):
        forward(longueur)
        right(90)
    done()
elif forme == 'ligne':
    longueur = int(input('Entrez la longueur de la ligne : '))
    forward(longueur)
    done()
else:
    print("Forme non reconnue. Veuillez entrer 'carré' ou 'ligne'.")