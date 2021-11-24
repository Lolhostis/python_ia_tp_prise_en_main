import numpy as np
import pandas as pd

index=["Haute-Loire", "Cantal", "Puy-de-Dome", "Allier"]

#QUESTION 1
data=[226835, 143627, 656643, 333065]
s_pop = pd.Series(data, index)

print("Population Auvergne :\n",s_pop)
print(42*"-")

#QUESTION 2
data=[4977, 5726, 7970, 7340]
s_sup = pd.Series(data, index)

print("Superficie Auvergne :\n",s_sup)
print(42*"-")

#QUESTION 3
d={
    'nb_habitants' : pd.Series([226835, 143627, 656643, 333065], index),
    'surface' : pd.Series([4977, 5726, 7970, 7340], index),
    'code_postal' : pd.Series(["43000", "15000", "63000", "03000"], index),
    'date_creation' : pd.Series([1790, 1790, 1790, 1790], index),
    'nb_arrondissement' : pd.Series([10, 20, 40, 60], index),
    'nb_cantons' : pd.Series([5, 9, 18, 7], index),
    'nb_communes' : pd.Series([4, 8, 3, 9], index)
}
df_auvergne = pd.DataFrame(d)

print(df_auvergne)
print(42*"-")
