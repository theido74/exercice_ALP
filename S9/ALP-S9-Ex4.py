L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

def choose_value(n,m,liste):
    for i in liste:
        if n<m:
            if i>=n and i<=m:
                print(i)
            else:
                if i>=m and i<=n:
                    print(i)

choose_value(2,6,L10_INT)