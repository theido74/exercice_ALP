import time

annee_actuelle = time.localtime().tm_year

def calcul_salaire(salaire_brut, annee_embauche):
    if annee_actuelle - annee_embauche < 5:
        print('Votre Salaire est de : ', salaire_brut, 'votre prime est de 0 CHF')
    elif annee_actuelle-annee_embauche > 5 and annee_actuelle-annee_embauche < 10:
        prime = salaire_brut * 3 / 100
        print('Votre Salaire est de : ', salaire_brut, 'votre prime est de ', prime, 'CHF', 'votre salaire total est de : ', salaire_brut + prime, 'CHF')
    else:
        prime = salaire_brut * 7 / 100
        print('Votre Salaire est de : ', salaire_brut, 'votre prime est de ', prime, 'CHF', 'votre salaire total est de : ', salaire_brut + prime, 'CHF')

salaire_brut = int(input('Entrez votre salaire brut en CHF: '))
annee_embauche = int(input('Entrez votre année d\'embauche: '))
calcul_salaire(salaire_brut, annee_embauche)