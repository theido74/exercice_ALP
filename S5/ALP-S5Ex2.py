def print_numbers():
    nombres_debut = int(input("Entrez le nombre de début: "))
    nombre_fin = int(input("Entrez le nombre de fin: "))
    for i in range(nombres_debut,nombre_fin + 1):
        print(i)

print_numbers()