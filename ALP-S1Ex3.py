largeur = int(input('Entrez la largeur de la pièce en m : '))
hauteur = int(input('Entrez la hauteur de la pièce en m : '))
profondeur = int(input('Entrez la profondeur de la pièce en m : '))
print(f'L\'aire de la pièce est de {largeur * hauteur} m², le volume de la pièce est de {largeur * hauteur * profondeur} m³, l\'aire des murs est de {2 * (largeur * hauteur + largeur * profondeur + hauteur * profondeur)} m²')