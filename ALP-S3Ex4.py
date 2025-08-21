nb_oui = int(input('Nombre de OUI: '))
nb_non = int(input('Nombre de NON: '))

def prime_oui():
    prime_base = 5000
    if sum([nb_oui, nb_non]) > 1000 and sum([nb_oui, nb_non]) < 2000:   
        prime_base += 8000
    elif sum([nb_oui, nb_non]) >= 2000:
        prime_base += 12000
    else:
        prime_base = prime_base
    return prime_base

def prime_nb():
    prime_nb = 0
    if nb_oui > nb_non and nb_oui/nb_non > 1.65:
        prime_nb += 4000
    elif nb_oui > nb_non:
        prime_nb += 2000
    else:
        prime_nb += 0
    return prime_nb

prime_total = prime_oui() + prime_nb()
print(f'La prime totale est de {prime_total}')
    
    