def draw_star_triangle_type1(nb_lignes):
    for i in range(1,(nb_lignes+1)):
        print('*'*i)
        
def draw_triangle_type2(nb_lignes):
    for i in range(nb_lignes+1,1,-1):
        print('*'*i)

def draw_triangle_type4(nb_lignes):
    for i in  range(nb_lignes,0,-1):
        print(' '*(nb_lignes-i)+'*'*i)

def draw_triangle_type3(nb_lignes):
    for i in range(1,nb_lignes+1):
        print(' '*(nb_lignes-i)+'*'*i)
    
def main():
    nb_lignes = int(input('Entrez le nombre de lignes pour le triangle: '))
    draw_star_triangle_type1(nb_lignes)
    draw_triangle_type2(nb_lignes)
    draw_triangle_type3(nb_lignes)
    draw_triangle_type4(nb_lignes)
if __name__=='__main__':
    main()
     