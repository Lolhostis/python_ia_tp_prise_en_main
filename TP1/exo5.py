print('-------- Exercice 5 : Dictionnaires --------\n\n')

print('1 - Créer un tuple tuple1 qui contient les noms différents de 5 personnes minimum.\n')
print("Les noms seront entrés à l'aide de ''input''\n")

nbPers=int(input("Veuillez entrer un entier pour désigner le nombre de personnes à créer : "))
#print(nbPers)
if nbPers>=5:
	tuple1 = ()
	for i in range(0,nbPers,1):
		nom=str(input("Veuillez saisir un nom de personne : "))
		#print(nom)
		for n in list(tuple1):
			#if nom in list(tuple1):
			if nom == n: 
				print('Erreur - Le nom d''utilisateur saisi est déjà dans le tuple\n')
				exit(1)

		tuple1 = tuple1 + (nom,) #virgule importante sinon ne fonctionne pas -> permet d'insérer en queue

else:
	print('Erreur - Le nombre de personnes minimum requises est de 5\n')
	exit(1)

print('tuple1 : ')
print (tuple1)
print('\n')

print('2 - Créer un tuple tuple2 qui contient les prénoms différents d''autant de personnes que dans tuple1\n')
print("Les noms seront entrés à l'aide de ''input''\n")

tuple2=()

for t1 in range(0,len(tuple1),1):
	prenom=str(input("Veuillez saisir un prénom de personne : "))
	print(prenom)
	for n in list(tuple2):
		if prenom in list(tuple2):
			print('Erreur - Le prenom d''utilisateur saisi est déjà dans le tuple\n')
			exit(1)

	tuple2 = tuple2 + (prenom,)

print('tuple2 : ')
print (tuple2)
print('\n')

print('3 - Former un dictionnaire dict1 de noms et de prénoms à partir de tuple1 et tuple2\n')

dict1={tuple1[x]:tuple2[x]for x in range(len(tuple1))}

print('dict1 : ')
print (dict1)
print('\n')

print('4 - Garder l''ordre des noms et changer l''ordre des prénoms\n')

import random 
values=list(dict1.values())
random.shuffle(values)

dictMelange =  dict()
for i in range(1,len(dict1)+1):
	dictMelange.update({dict1[i].key():values[i]})

print('dictMelange : ')
print (dictMelange)
print('\n')

print('5 - Créer une copie dict2 indépendante de dict1\n')

dict2 = copy(dict1)
dict2.clear()

print('dict1 : ')
print (dict1)
print('\n')

print('dict2 : ')
print (dict2)
print('\n')

print('6 - Ajouter une personne de nom ''Toto'' et de prenom ''Hello'' dans dict2\n')

print('7 - Ecrire une fonction qui prend en entrée deux dictionnaires et un booléen verbose pour afficher :\n')
print("\t * verbose est vrai : ce qui est commun\n")
print("\t * verbose est faux : ce qui est strictement différent\n")

