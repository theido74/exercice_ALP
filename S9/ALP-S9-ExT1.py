from turtle import *

COULEURS = ['yellow', 'green', 'blue', 'red']

def get_data():
    longueur_init = int(input('Entrez la longueur initiale: '))
    increment = int(input('Entrez l\'incrément: '))
    longueur_max = int(input('Entrez la longueur maximale: '))
    return longueur_init, increment, longueur_max

    
    

def draw_spiral(longueur_init, increment, longueur_max):
    longueur = longueur_init
    angle = 90
    while longueur <= longueur_max:
        pencolor(COULEURS[(longueur//increment) % len(COULEURS)])
        speed(-1)
        forward(longueur)
        right(angle)
        longueur += increment
    done()

def main():
    longueur_init, increment, longueur_max = get_data()
    draw_spiral(longueur_init, increment, longueur_max)
    
if __name__ == "__main__":  
    main()