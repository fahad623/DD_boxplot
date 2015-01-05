import pandas as pd


df = pd.DataFrame({'A':[1,2,3], 'B':[11,12,13]})

df.iloc[1] = 5

print df