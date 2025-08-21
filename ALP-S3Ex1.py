import math

pi = math.pi
def area_and_circo_of_circle():
    radius = int(input('Entrez le rayon du cercle:'))
    result_area =  pi * radius ** 2
    print(result_area, 'est l\'aire du cercle de rayon', radius, 'cm')
    result_circo = 2 * pi * radius
    print(result_circo, 'est la circonférence du cercle de rayon', radius, 'cm')
    
area_and_circo_of_circle()