import pandas as pd
from catboost.datasets import titanic


train, test = titanic()
dataset = pd.concat([train, test], ignore_index=True)
dataset.to_csv('./datasets/passengers.csv', index=False)

