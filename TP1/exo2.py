print('-------- Exercice 2 : Tuples --------\n\n')

print('1 - Créer un tuple tuple1 qui contient les entiers entre 1 et 5 inclus\n')

tuple1 = tuple((x for x in range(1,6)))
#ou : tuple1 = tuple(range(1, 6))

print('tuple1 : ')
print (tuple1)
print('\n')

print('2 - Créer un tuple tuple2 de chaines de caractères qui contient autant d''éléments que tuple1\n')

tuple2 = tuple([str(x) for x in tuple1])

print('tuple2 : ')
print (tuple2)
print('\n')

print('3 - Créer un tuple tuple3 qui contient tuple1 et tuple2\n')

tuple3=tuple1+tuple2

print('tuple3 : ')
print (tuple3)
print('\n')

print('4 - Définir une fonction qui calcule le minimum de tuple1\n')

def fct_min(tuple):
	return min(tuple)

print('min de tuple3 : ')
minT3=fct_min(tuple3)
print (minT3)
print('\n')

print('5 - Expliquer la différence entre un tuple et une liste\n')
print('Un tuple, contrairement à une liste : \n')
print('\t- Se déclare avec des parenthèses\n')
print('\t- Immuable (pas des références mais des valeurs donc tuple1=tuple2 ne va pas modifier tuple2 si tuple1 est modifié)\n')
print('\t- Non mutable : Impossible de le modifier en l''état (pas de méthode d''ajout ou de modification)\n')
print('\t- Pas possible de rechercher un élément (sauf voir s''il est présent avec ''in''\n')
print('\t- Plus rapide que les listes\n')
print('\n')

print('Une liste : \n')
print('\t- Crochets []\n')
print('\t- Mutable : liste1=liste2 alors si liste1 est modifiée, liste2 aussi\n')
print('\t- Possibilités d''ajout et modifications via des méthodes\n')
print('\n')
