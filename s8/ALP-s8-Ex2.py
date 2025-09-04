F0= 0
F1 = 1
def get_data():
    n = int (input("Entrez un nombre entier positif: "))
    m = int(input("Entrez un nombre maximum de la somme: "))
    return n,m

def check_data(n):
    if n > 0:
        return True

def fibonacci(n,m):
    print(f'F 0 = {F0}\nF 1 = {F1}')
    a=0
    b=1
    count = 2
    while count < n +1 and somme < m:
        somme = a+b
        print(f'F {count} = {somme}')
        a = b
        b = somme
        count += 1

def main():
    n,m = get_data()
    if check_data(n):
        fibonacci(n)

if __name__ == "__main__":
    main()

    
    
