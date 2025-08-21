nombre_de_pieces = int(input('Entrez le nombre de pièces : '))
prix_unitaire = float(input('Entrez le prix unitaire : '))
def calcul_tva(nombre_de_pieces):
    if nombre_de_pieces <= 250:
        return 1.082 
    elif nombre_de_pieces <= 500:
        return 1.063
    else:
        return 1.045 
    
def calcul_rabais(nombre_de_pieces):
    if nombre_de_pieces > 50:
        return 0.97
    elif nombre_de_pieces:
        return 0.95
    elif nombre_de_pieces > 1000:
        return 0.90
    else:
        return 1.0

def calcul_prix_total(nombre_de_pieces, prix_unitaire):
    tva = calcul_tva(nombre_de_pieces)
    rabais = calcul_rabais(nombre_de_pieces)
    prix_total = nombre_de_pieces * prix_unitaire * tva * rabais
    print(prix_total)
    return prix_total

calcul_prix_total(nombre_de_pieces, prix_unitaire)