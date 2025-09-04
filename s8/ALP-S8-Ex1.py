F0= 0
F1 = 1
def get_data():
    n = int (input("Entrez un nombre entier positif: "))
    return n

def check_data(n):
    if n > 0:
        return True

def fibonacci(n):
    print(f'F 0 = {F0}\nF 1 = {F1}')
    a=0
    b=1
    count = 2
    while count < n +1:
        somme = a+b
        print(f'F {count} = {somme}')
        a = b
        b = somme
        count += 1

def main():
    n = get_data()
    if check_data(n):
        fibonacci(n)

if __name__ == "__main__":
    main()

    
    
