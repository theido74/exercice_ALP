style_dic={
    '1':['collaborateur',0],
    '2':['client', 10],
}

vehicule_dic={
    '1': [100,0.8],
    '2': [200,1],
    '3': [200,1.5],
}

style_vehicule = input('Entrez votre style de véhicule désiré ( 1, 2 ou 3 ): ')
style_client = input('Si vous êtes collaborateur pressez 1, si vous êtes client pressez 2: ')
nombre_km = int(input('Entrez le nombre de km que vous allez parcourir: '))

def calcul_prix_location(style_vehicule, style_client):
    if style_vehicule in vehicule_dic and style_client in style_dic:
        prix_base = vehicule_dic[style_vehicule][0]
        prix_km = vehicule_dic[style_vehicule][1]
        reduction = style_dic[style_client][1]
        prix_total = (prix_base + (nombre_km * prix_km)) * (1 - reduction / 100)
        nom_client = style_dic[style_client][0]

        return prix_total, nom_client
    else:
        return 'Style de véhicule ou client inconnu.'

def main():
    print('Le prix total de la location est pour le style de véhicule' ,style_vehicule, 'et pour le style client :', calcul_prix_location(style_vehicule, style_client), 'CHF')
          
          
if __name__ == "__main__":
    main()  