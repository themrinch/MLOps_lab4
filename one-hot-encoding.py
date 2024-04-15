import pandas as pd


data = pd.read_csv('./datasets/passengers.csv')
data_encoded = pd.get_dummies(data, prefix='', prefix_sep='', columns=['Sex'])
data_encoded.to_csv('./datasets/passengers.csv', index=False)

