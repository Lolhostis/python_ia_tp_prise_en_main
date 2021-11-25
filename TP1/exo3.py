print('-------- Exercice 3 : Ensembles --------\n\n')

print('1 - Créer un ensemble ens1 qui contient les alphabets entre b et h inclus\n')
#ens1={'b','c','d','e','h'}
#ou ens1=set({'b','c','d','e','h'})
ens1=set('bcdeh')

print('ens1 : ')
print (ens1)
print('\n')

print('2 - Créer un ensemble ens2 d''entiers qui contient autant d''éléments que ens1\n')

ens2={0}
for i in range(1,len(ens1)):
	ens2.add(i)

print('ens2 : ')
print (ens2)
print('\n')

print('3 - Enlever les alphabets d''indices paires dans ens1\n')

maListe1=list(ens1)
tMaxEns1=len(ens1);
for i in range(0,tMaxEns1):
	if(i%2==0):
		ens1.discard(maListe1[i])

print('ens1 : ')
print (ens1)
print('\n')

print('4 - Enlever les entiers impairs dans ens2\n')

maListe2=list(ens2)
for i in range(0,tMaxEns1):
	if(i%2!=0):
		ens2.discard(maListe2[i])

print('ens2 : ')
print (ens2)
print('\n')

print('5 - Ecrire une fonction qui prend en entrée un ensemble et enlève toutes les voyelles\n')
def fct_sans_voyelles(ens):
	return ens-set('aeiouy')

ens4=set('aeyplouyz')

print('Ensemble ens4 avec voyelles : ')
print(ens4)
print('\n')

print('Ensemble sans voyelles : ')
ens4=fct_sans_voyelles(ens4)
print (ens4)
print('\n')


