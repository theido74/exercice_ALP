def get_data():
    n = int(input("Enrtez un nombre: "))
    return n

def print_odd_nb():
    n = get_data()
    for i in range(n, 0, -2):
        print(i)
def main():
    print_odd_nb()
if __name__ == "__main__":
    main()