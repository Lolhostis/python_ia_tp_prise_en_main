import numpy as np
import pandas as pd

print('-------- Exercice 2 --------\n\n')
print(" 1 - Avec la commande pd.read_csv ouvrez le fichier food.csv et assignez le à une dataframe appelée ''food''.\n")
print("Attention, le nom de l'extension est trompeur, vérifiez bien le séparateur utilisé (commande cat, grep ou un éditeur)\n")

food = pd.read_csv("data/food.csv", sep="\t")

print('food : ')
print (food)
print('\n')

print(" 2 - Afficher les 6 premières lignes\n")

lignes = food.head(6)

print('6 premières lignes : ')
print (lignes)
print('\n')

print(" 3 - Quel est le nombre d''observations (== de lignes) dans le jeu de données ?\n")

print (food.shape[0])
print('\n')

print(" 4 - Afficher le nombre de colonnes\n")

print (food.shape[1])
print('\n')

print(" 5 - Afficher les noms de colonnes\n")

for column in list(food.columns):
    print(column)
print('\n')

print(" 6 - Quel est le nom de la 105ème colonne ?\n")

nomCol=food.columns[104] #105ème colonne de numéro 104

print (nomCol)
print('\n')

print(" 7 - Quel est le type d''objet présent à la 105ème colonne ?\n")

print (type(nomCol))
print('\n')

print(" 8 - Quel est l''index du dataset (base de données)\n")

for index in food.index:
    print(index)
print('\n')

print(" 9 - Quel est le nom du produit à la 19ème ligne ?\n")

maColonne=food["product_name"]
maValeur=maColonne[18]
print (maValeur)
print('\n')





