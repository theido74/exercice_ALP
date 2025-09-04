NOTES = [3, 6, 5.5, 4.5, 2.5, 4, 5, 4, 3, 4, 2.5, 4.5, 5, 5, 4, 3]

def get_mean(liste):
    somme = 0
    for i in liste:
        somme += i
        moyenne = somme / len(liste)
    return moyenne.round(2)

def get_low_4(liste):
    new_list = [i for i in liste if i < 4]
    return new_list

def la_meilleure_note(liste):
    best = max(liste)
    return best

def get_index_of_best_note(liste):
    index = liste.index(max(liste))
    return index
    