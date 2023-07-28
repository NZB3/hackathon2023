import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv('./datasets/dataset1.csv')
dataset2 = pd.read_csv('./datasets/dataset2.csv')

df = pd.concat([dataset1, dataset2])

df_yearly = df.groupby('год')

df_monthly = df_yearly.apply(lambda x: x.groupby('месяц')['инцидентов'].sum())

fig, ax = plt.subplots(figsize=(12,6))
ax.set_title('количество инцидентов по месецам')
ax.set_xlabel('дата')
ax.set_ylabel('количество инцидентов')

df_monthly.plot(ax=ax)
plt.show()