def get_data():
    type_place = int(input("Entrez le type de place (1 pour normale, 2 pour VIP): "))
    nombre_place = int(input("Entrez le nombre de places: "))
    return type_place, nombre_place 

def check_type_place(type_place):
    if type_place not in [1, 2]:
        print("Type de place invalide. Veuillez entrer 1 pour normale ou 2 pour VIP.")
        return False
    return True
def check_nombre_place(nombre_place):
    if nombre_place < 1 or nombre_place > 70:
        print("Nombre de places invalide. Veuillez entrer un nombre entre 1 et 70.")
        return False
    return True

def main():
    type_place, nombre_place = get_data()
    check_type_place(type_place)
    check_nombre_place(nombre_place)
if __name__=="__main__":
    main()