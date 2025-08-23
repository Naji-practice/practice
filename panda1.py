import pandas as pd
# s = pd.Series([10,20,30,40])
# print(s)

data = {
    'Name':['Alice','Bob','Naji','Nivi','Rahan','Ashwanth','Kishore','Bhaggu'],
    'Age':[25,30,21,25,26,None,21,25],
    'Score':[85.5,85.6,26.8,69.8,55.3,55,84,63.5]
    }
df = pd.DataFrame(data)

# print(df)
# print(df.head())
# print(df.head(6))
# print(df.tail())
# print(df.tail(3))

# df.info()
print(df.describe())
# print(df.columns)
# print(df.shape)
# print(df.iloc[0])
# print(df.iloc[1,0])
# print(df.iloc[:,0:2])


# print(df.loc[6,'Name'])

# print(df.iloc[1,0])

# print(df.iloc[0:2])

print(df.isnull())

print(df.dropna())

df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)