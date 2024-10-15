import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.set(style='whitegrid')
plt.figure(figsize=(8, 5))
sns.lineplot(x='dia', y='venda', data=df, marker='o')
plt.title('Preço médio da gasolina em São Paulo - Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.savefig('gasolina.png')
print(gasolina.png)
