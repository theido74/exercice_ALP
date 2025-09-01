def get_data():
    type_piano = int(input("Entrez le type de piano (1 pour droit, 2 pour à queue): "))
    nb_km = int(input("Entrez le nombre de km à parcourir: "))
    nb_etages_up = int(input("Entrez le nombre d'étages à monter: "))
    nb_etages_down = int(input("Entrez le nombre d'étages à descendre: "))
    return type_piano, nb_km, nb_etages_up, nb_etages_down

def check_data(type_piano, nb_km, nb_etages_up, nb_etages_down):
    
    if type_piano not in [1, 2]:
        print("Type de piano invalide. Veuillez entrer 1 pour droit ou 2 pour à queue.")
        return False
    if nb_km < 0 or nb_km > 300:
        print("Nombre de km invalide. Veuillez entrer un nombre entre 0 et 300.")
        return False
    if nb_etages_up < 0:
        print("Nombre d'étages à monter invalide. Veuillez entrer un nombre positif.")
        return False
    if nb_etages_down < 0:
        print("Nombre d'étages à descendre invalide. Veuillez entrer un nombre positif.")
        return False
    if nb_etages_up > nb_etages_down * 3:
        print("Nombre d'étages à monter invalide. Veuillez vérifier les valeurs entrées.")
        return False
    return True

def main():
    type_piano, nb_km, nb_etages_up, nb_etages_down = get_data()
    if check_data(type_piano, nb_km, nb_etages_up, nb_etages_down):
        print("Les données sont valides.")
    else:
        print("Les données sont invalides.")

if __name__ == "__main__":
    main()