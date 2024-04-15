import pandas as pd


data = pd.read_csv('./datasets/passengers.csv')
new_data = data.loc[:, ['Pclass', 'Sex', 'Age']]
new_data.to_csv('./datasets/passengers.csv', index=False)

