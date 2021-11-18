# Question 1
tuple1 = tuple((x for x in range(1,6)))
print(tuple1)
# OU
tuple1 = tuple(range(1, 6))
print(tuple1)

# Question 2
tuple2 = tuple([str(x) for x in tuple1])
print(tuple2)

# Question 3
tuple3=tuple1+tuple2
print(tuple3)

# Question 4
def min_tuple(t):
    return(min(t))

print(min_tuple(tuple1))

# Question 5
# Un tuple est une liste immuable
# Points communs listes et tuples :
#   - ordonnés
#   - il n'y a pas forcement d'unicité sur les éléments qu'ils contiennent
#   - sont itérables
# Differences listes et tuples :
#   - Les éléments d'un tuples ne peuvent pas êtres changés
#       Les tuples sont immuables
#       Les listes sont mutables

# Fonctionnalités des tuples :
#   - ajouter un element à la fin d'un tuple :
#   a = a + tuple([5])
#   - utilisées dans une double affectation :
#   a=(1, 2)
#   x, y = a

