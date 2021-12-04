import numpy as np
import pandas as pd

print('-------- Exercice 1 --------\n\n')
print(" 1 - Créer une Série avec comme index le nom des départemments en Auvergne et pour les données, le nombre d'habitants du département correspondant\n")

index = ["Allier", "Cantal", "Haute-Loire", "Puy-de-Dôme"]
donnees = [343114, 149057, 220437, 626639]
serie1 = pd.Series(donnees, index=index)

print('serie1 : ')
print (serie1)
print('\n')

print(" 2 - Créer une Série avec comme index le nom des départemments en Auvergne et pour les données, la surface en km2 du département correspondant\n")

donnees2 = [7340, 5726, 4977, 7970]
serie2 = pd.Series(donnees2, index=index)

print('serie2 : ')
print (serie2)
print('\n')

print(" 3 - Créer une dataframe indexée par les départemments en Auvergne et qui contient :\n")
print("\tnombre d''habitants\n")
print("\tsurface\n")
print("\tcode postal\n")
print("\tdate de création\n")
print("\tnombre d''arrondissements\n")
print("\tnombre de cantons\n")
print("\tnombre de communes\n")

mesSeries = {
'nombre d''habitants': serie1, 
'surface': serie2, 
'code postal': pd.Series(['03000', '15000', '43000', '63000'], index=index), 
'date de création': pd.Series(['4/03/1790', '4/03/1790', '4/03/1790', '4/03/1790'], index=index), 
'nombre d''arrondissements': pd.Series([3, 3, 3, 5], index=index), 
'nombre de cantons': pd.Series([19, 15, 19, 31], index=index), 
'nombre de communes': pd.Series([317, 246, 257, 464], index=index)
}

maDataFrame = pd.DataFrame(mesSeries)

print('maDataFrame : ')
print (maDataFrame)
print('\n')



















