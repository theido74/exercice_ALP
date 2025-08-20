def israbais(prix,nombre):
    if nombre <= 100:
        return prix*nombre
    else:
        return prix*nombre*0.9
    
prix = float(input('Entrez le prix unitaire : '))
nombre = int(input('Entrez le nombre d\'articles : '))
print(f'Le prix total est de {israbais(prix,nombre)} CHF, le montant du rabais est de {israbais(prix,nombre) - prix*nombre} CHF.')
