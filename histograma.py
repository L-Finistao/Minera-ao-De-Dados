import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lê o arquivo CSV
df = pd.read_csv('.\PreProcessamentoMod\codigos\dataPTFiltrado300.csv')

# Extrai o atributo Age em um array NumPy
idades = df['Idade'].values

# Configuração do histograma
bin_width = 6
bins = np.arange(0, 100, bin_width)

# Cálculo da frequência
total_samples = len(idades)
freq = np.ones_like(idades) * (total_samples * bin_width / 100)

# Criação do histograma
plt.hist(idades, bins=bins, weights=freq, edgecolor='black')

# Configuração do gráfico
plt.title('Histograma de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')

# Exibição do gráfico
plt.show()
