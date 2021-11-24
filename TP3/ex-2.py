import numpy as np
import pandas as pd

#QUESTION 1
df_food=pd.read_csv("data/food.csv", sep='\t')
print(42*"-")

#QUESTION 2
print(df_food.head(6))
print(42*"-")

#QUESTION 3
print("la df_food contient", len(df_food.index), "index/lignes")
print(42*"-")

#QUESTION 4
print("la df_food contient", len(df_food.columns), "columns/colonnes")
print(42*"-")

#QUESTION 5
for column in list(df_food.columns):
    print(column)
print(42*"-")

#QUESTION 6
col_105=list(df_food.columns)[104]
print("Nom de 105eme colonne de df_food :", col_105)
print(42*"-")

#QUESTION 7
#Quand on extrait une columns d'une df, on obtient une Series
print(type(df_food[col_105]))
print(42*"-")

#QUESTION 8
for index in df_food.index:
    print(index)
print(42*"-")

#QUESTION 9
print("Produit à la 19eme ligne/index de df_food :",list(df_food.index)[18])
print(42*"-")
