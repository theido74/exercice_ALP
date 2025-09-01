PLACE_DEBOUT = 20
PLACE_ASSISE = 30

type_place = input('Pour une place debout tapez : 1, pour une place assise tapez : 2 \t')
nombre_places = int(input('Combien de places voulez-vous ?'))


def prix_place(type_place, nombre_places):
    if type_place == '1':
        if nombre_places >= 5:
            return ((PLACE_DEBOUT * nombre_places)/nombre_places * (nombre_places-1))
        elif nombre_places >= 9:
            return ((PLACE_DEBOUT * nombre_places)/nombre_places * (nombre_places-2))
        else:
            return (PLACE_DEBOUT * nombre_places)
    elif type_place == '2':
        if nombre_places >= 5:
            return ((PLACE_ASSISE * nombre_places)/nombre_places * (nombre_places-1))
        elif nombre_places >= 9:
            return ((PLACE_ASSISE * nombre_places)/nombre_places * (nombre_places-2))
        else:
            return (PLACE_ASSISE * nombre_places)
    else:
        return 'Type de place non reonnu'

def main():
    print('\033[1m' + 'Le' + '\033[0m' +' prix à payer pour ' + '\033[91m' + str(nombre_places) + '\033[0m' + ' places est de :''\033[91m', str(prix_place(type_place, nombre_places)) + '\033[0m' +' Frs')

if __name__ == "__main__": 
    main()