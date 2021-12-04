import numpy as np
import pandas as pd

print('-------- Exercice 3 --------\n\n')
print(" 1 - Avec la commande od.read_csv ouvrir le fichier chipotle.tsv dans une dataframe df_Chipotle\n")

df_Chipotle = pd.read_csv("data/chipotle.tsv", sep="\t")

print('df_Chipotle : ')
print (df_Chipotle)
print('\n')

print(" 2 - Afficher les 7 premières lignes. Afficher les noms des colonnes.\n")

lignes = df_Chipotle.head(7)
print (lignes)
print (df_Chipotle.columns)

#ou : print(df_Chipotle[:7])
print('\n')

print(" 3 - Créer une nouvelle colonne dans la dataframe contenant le prix de vente en float à partir de la colonne ''item_price''\n")

df_Chipotle['item_price_float']=df_Chipotle['item_price'].str.replace("\$", "").astype(float)

print (df_Chipotle["item_price_float"])
print('\n')

print(" 4 - Afficher les lignes d''index impair\n")

for i in range(0,len(df_Chipotle.columns)):
	if(i%2!=0):
		print(df_Chipotle.columns[i])
		print('\n')

#ou : print(df_Chipotle[df_Chipotle.index%2==1])
#ou : print(df_Chipotle[1::2])

print(" 5 - Afficher les lignes dont le prix est supérieur au prix moyen (pm)\n")

moy_item_value = df_Chipotle['item_value'].mean()
print(df_Chipotle[df_Chipotle['item_value']>moy_item_value])
print('\n')

print(" 6 - Afficher les lignes dont le prix est supérieur au prix moyen (pm) des produits + la déviation standard / sqrt(N) où N est le nombre d''observations : prix >= { (pm times %sigma) } / {sqrt(N)}\n")

moy_item_value = df_Chipotle['item_value'].mean()
ecart_type_item_value = df_Chipotle['item_value'].std()
sqrt_n = np.sqrt(df_Chipotle['item_value'].shape[0])

deviation=(moy_item_value*ecart_type_item_value)/sqrt_n

print(df_Chipotle[df_Chipotle['item_value']>=deviation])
print("\n")






