chiffre = int(input('Enrez un chiffre : '))
def ispostif(chiffre):
    if chiffre >= 0:
        print('Le chiffre est positif ou nul')
    else:
        print('le chiffre est négatif')
ispostif(chiffre)