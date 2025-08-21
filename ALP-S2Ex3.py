def calcul_prix_billet():
    type_voyageur = int(input('Si vous êtes employés de la compagnie pressez 1, si vous êtes membres du club cygognes pressez2, sinon pressez 3.'))
    vol_effectue = int(input('Entrez le nombre de vols effectués avec notre compagnies: '))
    prix_effectif = int(input('Entrez le prix effectif du billet: '))
    prix_apres_type = 0
    if type_voyageur == 1:
        prix_apres_type = prix_effectif * 0.8
    elif type_voyageur == 2:
        prix_apres_type = prix_effectif * 0.9
    elif type_voyageur == 3:
        prix_apres_type = prix_effectif
    else:
        print('Type de voyageur inconnu.')
    
    prix_apres_rabais = 0
    if vol_effectue == 1:
        prix_apres_rabais = prix_apres_type * 0.9
    elif vol_effectue > 2 and vol_effectue < 5:
        prix_apres_rabais = prix_apres_type * 0.85
    elif vol_effectue >= 5:
        prix_apres_rabais = prix_apres_type * 0.8
    else:
        prix_apres_rabais = prix_apres_type
    
    print('Le prix du billet est de : ', prix_apres_rabais, 'CHF')
    
calcul_prix_billet()