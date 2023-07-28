import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv('./datasets/dataset1.csv')
dataset2 = pd.read_csv('./datasets/dataset2.csv')

df = pd.concat([dataset1, dataset2])

df[["отказ"]] = df[["отказ"]].fillna(0)
grouped = df.groupby('год')
# создаем столбчатую диаграмму
plt.bar(df['год'], df['отказ'])
# добавляем заголовок и подписи к осям
plt.title('Количество отказов в год')
plt.xlabel('год')
plt.ylabel('отказы')

# отображаем диаграмму
plt.show()