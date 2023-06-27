import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv('.\PreProcessamentoMod\codigos\dataPTFiltrado300.csv')

# Gerando a matriz de correlação
corr_matrix = df.corr()

# Configurando o tamanho do gráfico
plt.figure(figsize=(12, 20))

# Gerando o mapa de calor da matriz de correlação
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, annot_kws={"fontsize": 6})

# Exibindo o gráfico
plt.show()
