def get_data():
    capital_dep = int(input("Entrez le capital de départ: "))
    taux_int = float(input("Entrez le taux d'intérêt (en pourcentage): "))
    nb_perdiodes = int(input("Entrez le nombre de périodes: "))
    return capital_dep, taux_int, nb_perdiodes
    
def calcul_interet(capital_dep, taux_int, nb_perdiodes):
    for _ in range(nb_perdiodes):
        capital_dep += capital_dep * (taux_int / 100)
    return capital_dep

def main():
    capital_final = calcul_interet(*get_data())
    print(f"Le capital final après {nb_perdiodes} périodes est de: {capital_final:.2f}")
