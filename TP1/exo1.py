print('-------- Exercice 1 : Listes --------\n\n')

print('1 - Créer une liste liste1 qui contient les entiers entre 1 et 100\n')

liste1=list(range(1,101)); 

print('liste1 : ')
print (liste1)
print('\n')

print('2 - Inverser l''ordre des éléments de liste1\n')

liste1 = liste1[::-1]

print('liste1 : ')
print (liste1)
print('\n')

print('3 - Créer une liste liste2 qui contient autant d''éléments que liste1\n')

liste2 = liste1.copy()

print('liste2 : ')
print (liste2)
print('\n')

print('4 - Créer une liste liste3 qui contient la somme de liste1 et liste2\n')

liste3=[elt1 for elt1 in liste1]
#Equivalent à : liste3=liste1.copy() 
#Equivaut à liste3=liste1 mais sans modifier liste1

i=0
for elt in liste2[1::]:
	liste3[i]=liste3[i]+elt
	i=i+1

#ou directement : liste3=[liste1[x]+liste2[x] for x in range(len(liste1))]

print('liste3 : ')
print (liste3)
print('\n')

print('5 - Calculer le maximum de liste3\n')

print('max : ')
print (max(liste3))
print('\n')

print('6 - Définir une fonction qui calcule le maximum d''une liste\n')

def fct_max(liste):
	return max(liste)

print('max de liste1 : ')
maxL1=fct_max(liste1)
print (maxL1)
print('\n')


