Liste = [3, 3, 6, 6, 4, 9, 5, 6, 4, 7, 6, 4, 3, 3, 1, 2, 8, 4, 5, 6, 7, 8, 9, 10, 11] 


def controle_escalade(liste, capacite):
    entree = 0
    counter = 0
    nb_groupes = len(liste)
    for i in liste:
        if entree + i > capacite:
            print('Salle Pleine')
            print('Les groupes suivants ne peuvent pas entrer')
            print('groupe n°', counter + 1, ' au groupe ',nb_groupes)
            break
        entree += i
        counter += 1
        print('groupe n°', counter, ' : ', i, 'personnes')
        print('Nombre de personnes dans la salle : ', entree)


def controle_escalade_low(liste, capacite):
    entree = 0
    counter = 0
    nb_groupes = len(liste)
    for i in liste:
        if entree + i > capacite + i:
            print('Salle Pleine')
            print('Les groupes suivants ne peuvent pas entrer')
            print('groupe n°', counter + 1, ' au groupe ',nb_groupes)
            break
        entree += i
        counter += 1
        print('groupe n°', counter, ' : ', i, 'personnes')
        print('Nombre de personnes dans la salle : ', entree)