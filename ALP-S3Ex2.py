def creer_facture():
    numero_client = input("Entrez le numéro du client : ")
    prix_premier_artc = int(input("Entrez le prix du premier article : "))
    prix_deuxieme_artc = int(input("Entrez le prix du deuxième article : "))
    
    if prix_premier_artc <= prix_deuxieme_artc:
        prix_premier_artc = prix_premier_artc /2
    elif prix_premier_artc >= prix_deuxieme_artc:
        prix_deuxieme_artc = prix_deuxieme_artc /2
    
    
    total_facture = prix_premier_artc + prix_deuxieme_artc

    print('MAISON PTIPRI')
    print(f'Achat éffectués par le client {numero_client}')
    print(f'Prix des 2 articles achetés : {prix_premier_artc} CHF , {prix_deuxieme_artc} CHF ==> Prix à payer: {total_facture} CHF')
    print('Merci pour votre achat !')
    print('En cas de problèmes gnagnagna')

        
creer_facture()