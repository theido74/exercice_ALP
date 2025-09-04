RELEVES = [11.8, 14.4, 18.6, 16.5, 11.5, 12.3, 9.1] 

def get_mean(liste):
    somme = 0
    for i in liste:
        somme += i
        moyenne = somme / len(liste)
    return moyenne

def get_less_15(liste):
    list_less = [i for i in liste if i < 15]
    return list_less

def main():
    print(get_mean(RELEVES).__round__(2))
    print(get_less_15(RELEVES))

if __name__ == "__main__":
    main()
    