import pandas as pd

dataset1 = pd.read_csv('./datasets/dataset1.csv')
dataset2 = pd.read_csv('./datasets/dataset2.csv')

df = pd.concat([dataset1, dataset2])

count = df[df['отказ'] == 1]['отказ'].count()


print(count)