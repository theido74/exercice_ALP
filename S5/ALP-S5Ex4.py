n = int(input("Entrez un nombre pour afficher sa table de multiplication: "))
m = int(input('Entrez le nombre de multiplication à afficher:'))

def afficher_table(n):
    for i in range(1,m+1):
        print(f"{n} x {i} = {n*i}")

def main():
    afficher_table(n)
    
if __name__ == "__main__":
    main()