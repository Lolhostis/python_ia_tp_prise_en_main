import numpy as np
import pandas as pd

#QUESTION 1
df_Chipotle=pd.read_csv("data/chipotle.tsv", sep='\t')
print(df_Chipotle.head(5))
print(42*"-")

#QUESTION 2
print(df_Chipotle[:7])
print(42*"-")

#QUESTION 3
df_Chipotle['item_value'] = df_Chipotle['item_price'].str.replace('$','').astype(float)
print(df_Chipotle[:3])
print("Type de la column 'item_value' de Chipotle :", df_Chipotle['item_value'].dtype)
print(42*"-")

#QUESTION 4
print(df_Chipotle[df_Chipotle.index%2==1])
#OU
#print(df_Chipotle[1::2])
print(42*"-")

#QUESTION 5
moy_item_value = df_Chipotle['item_value'].mean()
print(df_Chipotle[df_Chipotle['item_value']>moy_item_value])
print(42*"-")

#QUESTION 6
moy_item_value = df_Chipotle['item_value'].mean()
ecart_type_item_value = df_Chipotle['item_value'].std()
sqrt_n = np.sqrt(df_Chipotle['item_value'].shape[0])

deviation=(moy_item_value*ecart_type_item_value)/sqrt_n

print(df_Chipotle[df_Chipotle['item_value']>=deviation])
print(42*"-")

