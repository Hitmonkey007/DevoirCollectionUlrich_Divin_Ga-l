#__Q.1__#

##__Creation de la liste__##
liste_vehicules = ['1. Kawasaki', '2. Bugati','3. Toyota','4. Subaru','5. BMW','6. Fiat','7. Chevrolet','8. Mercedes','9. Yamaha','10. Hyundai']
print(' Question I  :')
print('------------\n')
#--1-- Affichage des elements de la liste--#
print("--1--: La liste des Vehicules:")
print('____________________________\n')
for element in liste_vehicules:
    print(element)
    #--2-- Changer l'element numero 5--#
print("--2--: Liste apres le changement du numero 5:")
print('___________________________________________\n')
liste_vehicules.insert (5,'5. Lamborghini')
for element in liste_vehicules:
    print(element)
#--3-- Creer une nouvelle liste en remplissant avec les elements precedent--#
print("--3--: Nouvelle liste:")
print('____________________\n')
liste_new = []
for elt in liste_vehicules:
    if 'a' in elt:
        liste_new.append('1. Tesla')
for i in liste_new:
    print(i)
