import time

annee_actuelle = time.localtime().tm_year
def calcul_prix_billet():
    annee_naissance = int(input('Entrez votre année de naissance:'))
    age = annee_actuelle - annee_naissance
    jour = input('Entrez le jour de la semaine (lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche): ').lower()
    prix_age = 0
    if age < 7:
        prix_age = 5
    elif age >= 7 and age <= 18:
        prix_age = 10
    else:
        prix_age = 15
    if jour == 'lundi':
        prix_age *= 0.8
    elif jour == 'mardi' or jour == 'jeudi':
        prix_age *= 0.9
    else:
        prix_age *= 1.0
    print('Le prix du billet est de : ', prix_age, 'CHF')

calcul_prix_billet()