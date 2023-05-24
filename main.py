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
print('\n')    
    #--2-- Changer l'element numero 5--#
print("--2--: Liste apres le changement du numero 5:")
print('___________________________________________\n')
liste_vehicules.insert (5,'6. Lamborghini')
for element in liste_vehicules:
    print(element)
print('\n')    
#--3-- Creer une nouvelle liste en remplissant avec les elements precedent--#
print("--3--: Nouvelle liste:")
print('____________________\n')
liste_new = []
for elt in liste_vehicules:
    if 'a' in elt:
        liste_new.append('1. Tesla')
for i in liste_new:
    print(i)
print('\n')    
#--4-- Ajouter un element a la fin de la liste--#
print('--4--: Ajout d_un element a la fin de la liste:')
print('_____________________________________________\n')
liste_vehicules.insert(11,'11. Ferrari') 
for i in liste_vehicules:
    print(i)
print('\n')    
#--5-- Ajouter un element a l'index numero 2--#
print('--5--: Ajout_element a l_index numero 2: ')
print('_______________________________________\n')
liste_vehicules.insert(2,'3. Jaguar')
for j in liste_vehicules:
    print(j)
print('\n')        
#--6-- Supprimer l'élément numéro 3--#
print('--6--: La suppression du vehicule numero 3 :')
print('__________________________________________\n')
del liste_vehicules[3]
for i in liste_vehicules:
    print(i)
print('\n')    
#--7-- Supprimer l'élément à l’index numéro 2--#
print('--7--: La suppresion du vehicule a l_index numero 2:')
print('__________________________________________________\n') 
del liste_vehicules[2]
for i in liste_vehicules:
    print(i)
print('\n')            
#--8--  Ordonner la liste --#
print('--8--: Liste ordonnee:  ')
print('______________________\n') 
liste_vehicules.sort()
for i in liste_vehicules:
    print(i)
print('\n')    
#--9-- Afficher la liste au sens inverse --#
print('--9--: Liste affichee en sens inverse:  ')
print('______________________________________\n') 
liste_vehicules.reverse()
for i in liste_vehicules:
    print(i)
print('\n')    
#--10-- Vider la liste --#
print('--10--: la liste est videe')
print('________________________\n')
print('liste_vehicules[]')
liste_vehicules.clear()
for i in liste_vehicules:
    print(i)
print('\n')    
#--11-- Supprimer la liste --# 
print('--11--: La liste a ete supprimee  ')
print('________________________________\n')
del liste_vehicules
print('\n')
#----Fin de la Question I----#

#--Q.2--#
print(' Question II  :')
print('-------------\n')
#--1--Afficher le nombre de fois le chiffre que 3 apparait--#
tupl = (0,1,3,3,4,6,3,10,8,9)
nbre_fois_3 = 0
check_3 =tupl[0]
print('les elements du tuple sont :',tupl)
for i in range(len(tupl)):
    chiffre_3 =tupl[i]
    if chiffre_3 == 3:
        nbre_fois_3 +=1
print("#--1-- voici le nombre de fois qu'apparait le chiffre 3 :",nbre_fois_3,"fois\n")
print('____________________________________________________________________________\n')
print('\n')
#--2--Afficher le contenu de l'element numero 5--#

print("#--2-- voici l'element_5 :",tupl[5])
print('________________________________\n')
print('\n')

#--3-- ordonner la tuple--#

order = sorted(tupl)
print('#--3-- voici la tuple ordonnee :', order)
print('_____________________________________\n')
print('\n')
#--4--Ajouter un element a la fin de la ligne --#
print("#--4-- voici l'element ajoute a la fin du tuple :")
print('_______________________________________________\n')
tupl = tupl + (4,)
print(tupl)
print('\n')

#----5----Ajouter un element a l'index 3 ------------------------ :

print('#--5-- voici la liste apres ajout d_un element a l_index_3:')
print('_________________________________________________________\n')
t_2 = list(tupl)
t_2.insert(3,50)
tupl = tuple(t_2)
print(tupl)
print('\n')

#----6----affiche la nouvelle tuple apres l'ajout ----------------------- :
print('#--6-- la nouvelle tuple apres l_ajout')
print('____________________________________\n')
print(tupl)
print('\n')
# ----------------QUESTION III----------------------
print(' Question III :')
print('-------------\n')

st = {'Samsung','APPLE','Tecno','Itel','HUWAWEi','OPPO','XIAOMI','REalme','OnePlus','Honor'}

# ----1---afficher  un  set :

print("#--1-- voici la liste de mon set :")
print('________________________________\n')
for i in st :
    print(i)
print('\n')    
# ----2---ajouter un element :

st.add('Sony')
print("#--2-- voici la liste de mon set apres avoir ajouter un element:")
print('______________________________________________________________\n')
for i in st :
    print(i)
print('\n')

#----3---supprimer un element :

st.remove("Samsung")
print("#--3-- voici la liste de mon set apres avoir supprimer un element:")
print('________________________________________________________________\n')
for i in st :
    print(i)
print('\n')
#---4---supprimer un set :

print('#--4-- voici le set supprime:')
print('___________________________\n')
while st:
    st.discard(max(st))
print(st)
print("\n")

# ----------------QUESTION IV-------------------------------------
print(' Question IV :')
print('------------\n')
 
Dictionnaire = {'nom;':'IGIRANEZA',
                'prenom;':'Richy',
                'adresse;':'Ngagara',
                'email;':'igiranezaulrich19@gmail.com',
                'telephone;':'123456789',
                'taille;':'1.75cm',
                'profession;':'etudiant',
                'nom_universite;':'ULT',
                'Faculte;':'Info',
                'Departement;':'GL'}

# -------1-- affichage d'un dictionnaire:
print("#--1-- affichage d'un dictionnaire")
print("________________________________\n")
for i in Dictionnaire.items():
    print(i)
print('\n')
# -------2-- affichage les cles uniquement d'un dictionnaire :
print("#--2-- affichage des cles du dictionnaire :")
print("_________________________________________\n")
for i in Dictionnaire.keys():
    print(i) 
print('\n')
# -------3-- affichage les valeurs uniquement  d'un dictionnaire :
print("#--3-- affichage les valeurs d'un dictionnaire :")
print("______________________________________________\n")
for i in Dictionnaire.values():
    print(i)
print('\n')

# -------4-- affichage de la cle valeur correspondante d'un dictionnaire : 

print("#--4-- Affichage de la cle et valeur correspondante d'un dictionnaire :")
print("_____________________________________________________________________\n")
for cle,valeur in Dictionnaire.items():
    print("cle est :",cle,"la valeur correspondante est :",valeur)
print('\n')
# -------5-----Supprimer l'element a la cle numero 2:
print("#--5-- voici le dictionnaire apres la suppression_index_2:")
print("________________________________________________________\n")
Dictionnaire.pop("adresse;")
print(Dictionnaire)  
print('\n')

# ------6-------Afficher la valeur numero 5 :
numero_5 = Dictionnaire["taille;"]
print("#--6-- le numero 5 de mon dictionnaire a comme valeur :",numero_5,) 
print("_______________________________________________________________\n") 
print('\n')  

#-------7-------ajouter un nouvel element:
print("#--7-- voici le dictionnaire apres l'ajout d'un element:")
print("______________________________________________________\n")
Dictionnaire["age;"] = 18
for i in Dictionnaire:
    print(i)
print('\n')
#------8-------creer une copie d'un dictionnaire :
Dict_2 = Dictionnaire.copy()
print('#--8-- Dict_2 est la copie du dictionnaire :',Dict_2)
print('\n')

#------9-------Affichage des nouveaux elements :
Dict_2 = {'nom;':'Karire',
          'prenom;':'Carla',
          'adresse;':'Kinindo',
          'email;':'KarCa@gmail.com',
          'telephone;':'78541652',
          'taille;':'1.60cm',
          'profession;':'etudiant',
          'nom_universite;':'ULB',
          'Faculte;':'Economie',
          'Departement;':'Audite'}
print("#--9-- Les nouveaux elements de Dict_2 sont: ")
print("___________________________________________\n")
for i in Dict_2.items():
    print(i)
    
