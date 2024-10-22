import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

# Adicionar título e rótulos
plt.title('Variação do Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar o gráfico como imagem
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
