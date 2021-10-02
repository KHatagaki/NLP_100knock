import pandas as pd

df = pd.read_table('./popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])
print(df.sort_values(by='number',ascending=False))