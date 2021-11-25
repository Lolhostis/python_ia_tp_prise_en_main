print('-------- Exercice 4 : Chaines de caractères --------\n\n')

print('1 - Créer uune chaine de caractères chaine1 qui contient la phrase ''c''est que j''aime Python et son module''\n')

chaine1='c''est que j''aime Python et son module'

print('chaine1 : ')
print (chaine1)
print('\n')

print('2 - Afficher chaine1 avec un retour à la ligne\n')

chaine1=chaine1+'\n'

print('chaine1 : ')
print (chaine1)
print('\n')

print('3 - Afficher chaine1 avec un mot par ligne en utilisant la méthode split\n')

maListeChaine1=list(chaine1.split())
tMaxList=len(maListeChaine1)
chaine1=''
for i in range(0,tMaxList):
		#print(maListeChaine1[i])
		chaine1+=maListeChaine1[i] + '\n'

print('chaine1 : ')
print (chaine1)

print('4 - Enlever les e dans chaine1\n')

chaine2=''
tMax=len(chaine1)
for i in range(0,tMax):
	if(chaine1[i]!='e'):
		chaine2 += chaine1[i]

chaine1=chaine2

print('chaine1 : ')
print (chaine1)
print('\n')

print('5 - Ecrire une fonction qui prend en entrée une chaine de caracteres et compte le nombre des alphabets\n')
def fct_cpt_alpha(chaine):
	cpt=0
	ok=0
	tMax=len(chaine)
	for i in range(0,tMax):
		print(chaine[i])
		maListeChaine=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		for j in maListeChaine:
			if(chaine[i]==j):
				cpt+=1
				print('cpt :')
				print(cpt)

	return cpt

chaine3='J''ai 13 caracteres' 
nbAlpha=fct_cpt_alpha(chaine3)

print('Chaine chaine3 : ')
print(chaine3)
print('\n')

print('Nombre de caracteres : ')
print (nbAlpha)
print('\n')


