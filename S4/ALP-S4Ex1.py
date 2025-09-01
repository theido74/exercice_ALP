KM = 6

piano_type = input('Pour un piano droit tapez : 1, pour un piano à queue tapez : 2 \t')
nombre_etage = int(input('Combien d\'étages à monter ?'))
nombre_km = int(input('Combien de kilomètres à parcourir ?'))
prix_transport = KM*nombre_km


def demenagement(piano_type, nombre_etage, nombre_km):
    if piano_type == '1':
        return (60*nombre_etage + prix_transport)
    elif piano_type == '2':
        return (90*nombre_etage + prix_transport)
    else:
        return 'Type de piano non reonnu'

def afficher_resultat():
    result = demenagement(piano_type, nombre_etage, nombre_km)
    if result < 200:
        print('\033[1m'+'Prix '+ '\033[0m'+'minimum est de 200 CHF')
    elif result > 2500:
        print('\033[1m'+'Prix '+ '\033[0m'+'maximum est de 2500 CHF')
    else:
        print('\033[1m'+'Prix' + ' total est de : '+ '\033[0m'+ str(result) + ' CHF dont',prix_transport,'de transport pour les', KM , ' km')       

def main():
    afficher_resultat()

if __name__ == "__main__": 
    main()

