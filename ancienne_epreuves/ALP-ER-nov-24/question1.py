# Imports

# Constantes
FRAIS_GESTION_L1 = 1
FRAIS_GESTION_L2 = 1.5 
FRAIS_GESTION_L3 = 3

TARIF_JOUR_L1 = 0.1
TARIF_JOUR_L2 = 0.2 
TARIF_JOUR_L3 = 0.3

REDUCTION_PREMIUM = 0.2
 
# Procédures et fonctions
def get_data():
     type_livre = input("Entrez le type de livre (1, 2, 3) : ")
     type_adherent = input("Entrez le type d'adhérent (standard, premium) : ")
     nb_jours = int(input("Entrez le nombre de jours d\'emprunt (max.92) : "))
     return (type_livre, type_adherent, nb_jours)

def check_data(type_livre, type_adherent, nb_jours):
    erreurs = []  

    if type_livre not in ['1', '2', '3']:
        erreurs.append("Erreur: catégorie de livre invalide (doit être 1, 2 ou 3)")
    if type_adherent not in ['standard', 'premium']:
        erreurs.append("Erreur: type d'adhérent invalide (doit être 'standard' ou 'premium')")
    if nb_jours < 1 or nb_jours > 93:
        erreurs.append("Erreur: nombre de jours invalide (doit être entre 1 et 92)")

    if erreurs:
        for erreur in erreurs:
            print(erreur) 
        return None
    else:
        print("Données valides")
        return (type_livre, type_adherent, nb_jours)


def calcul_avant_remise(type_livre,nb_jours):
    if type_livre == '1':
        frais_gestion = FRAIS_GESTION_L1
        tarif_jour = TARIF_JOUR_L1
        total_loc = tarif_jour * nb_jours + frais_gestion
        return total_loc
        
        
    elif type_livre == '2':
        frais_gestion = FRAIS_GESTION_L2
        tarif_jour = TARIF_JOUR_L2
        total_loc = tarif_jour * nb_jours + frais_gestion
        return total_loc

    else:
        frais_gestion = FRAIS_GESTION_L3
        tarif_jour = TARIF_JOUR_L3
        total_loc = tarif_jour * nb_jours + frais_gestion
        return total_loc


# Procédure main()
def main():
    type_livre, type_adherent, nb_jours = get_data()
    valid_data = check_data(type_livre, type_adherent, nb_jours)
    total_avant_remise = calcul_avant_remise(type_livre, nb_jours)
    if valid_data:
        if type_adherent == 'premium':
            remise = total_avant_remise * REDUCTION_PREMIUM
            total_apres_remise = total_avant_remise - remise
            if total_avant_remise <=24:
                print(f"Le montant total après remise est de : {total_apres_remise:.2f} euros")
            else:
                print(f"Le montant total après remise est de : {total_apres_remise:.2f} euros")
                print(f'Le montant maximum pour une location est de 24 CHF')
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
