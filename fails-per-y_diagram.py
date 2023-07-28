import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv('./datasets/dataset1.csv')
dataset2 = pd.read_csv('./datasets/dataset2.csv')

df = pd.concat([dataset1, dataset2])

# создаем столбчатую диаграмму
plt.bar(df['год'], df['инцидентов'])
# добавляем заголовок и подписи к осям
plt.title('Количество отказов в год')
plt.xlabel('Год')
plt.ylabel('Количество отказов')

# отображаем диаграмму
plt.show()