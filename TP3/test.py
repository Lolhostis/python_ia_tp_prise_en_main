import numpy as np;
import pandas as pd;

d = {
'one': pd.Series([1., 2., 3.,0], index=['a', 'b', 'c','e']),
'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)
print('­$­'*5)
print(df.dtypes)

print(2*np.random.rand(2,2))

print("-"*20)
print(pd.DataFrame(d, index=['c', 'a', 'b','h']))
print("-"*20)
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))
print("-"*20)
print(df, end="\n"+42*"$"+"\n")
print("Index :", df.index)
print("Colonnes :", df.columns[0])

print(42*'/')
d = {
'one': [1., 2., 3., 4.],
'two': [4., 3., 2., 1.]
}
df=pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
print(df)
print(42*'/')
print(df['one']) #colonne qui correspond à l'étiquette one'
print('­+'*10)
print(df[["one","two"]])
print(42*'/')
df['flag'] = df['one'] > 2
print(df)
print(42*'/')
print(df,'\n','*'*20)
del df['two']
print(df,'\n','*'*20)
three = df.pop('one')
print(df,'\n','*'*20)
print(three)
