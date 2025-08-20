annee_actuelle = 2020

salaire_base = int(input('Entrez votre salaire de base : '))
annee_engagement = int(input('Entrez votre année d\'engagement : '))
nombre_annees = annee_actuelle - annee_engagement
def is_prime(salaire, nombre_annees):
    if nombre_annees < 5:
        print('Vous n\'avez pas droit à une augmentation. Votre salaire reste :', salaire, 'CHF.')
        return salaire
    else:
        print('Vous avez droit à une augmentation. Votre salaire passe de', salaire * 1.03, 'CHF à')
        return salaire * 1.03

is_prime(salaire=salaire_base, nombre_annees=nombre_annees)