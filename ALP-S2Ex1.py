nombre = int(input('Entrez un nombre entier'))
def is_pos(nombre):
    if nombre > 0:
        print("Le nombre est positif.")
    elif nombre < 0:
        print('Le nombre est négatif')
    else:
        print("Le nombre est nul.")
is_pos(nombre)