L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5] #liste de un seul nombre réel 

L0 = [] #liste vide

def get_first_element(liste):
    if len(liste) > 0:
        return liste[0]

def get_last_element(liste):
    if len(liste) > 0:
        return liste[-1]

def get_the_char_before_the_last_one(liste):
    if len(liste) > 1:
        return liste[-2]

def get_list_value(liste,n):
    if len(liste) > n:
        return liste[n -1]


