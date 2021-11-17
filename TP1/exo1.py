# Question 1
liste1 = list(range(1, 101))
print(liste1)

print('\n');

# Question 2
liste1 = liste1[::-1]
print(liste1)

print('\n');

# Question 3
liste2 = liste1.copy() # On fait une deepcopy de liste1
print(liste2)

print('\n');

# Question 4
liste3=[liste1[x]+liste2[x] for x in range(len(liste1))]
print(liste3);

print('\n');

# Question 5
print(max(liste3))

print('\n');

# Question 6
def max_list(l):
    return(max(l))

print('max de liste3 :', max_list(liste3))
