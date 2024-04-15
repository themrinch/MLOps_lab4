import pandas as pd


data = pd.read_csv('./datasets/passengers.csv')
mean_age = data['Age'].mean()
data['Age'] = data['Age'].fillna(mean_age)
data.to_csv('./datasets/passengers.csv', index=False)

