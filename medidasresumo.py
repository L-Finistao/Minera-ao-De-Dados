import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar a base de dados
data = pd.read_csv('Database.csv')

# Selecionar o atributo "Tipo de cliente"
tipo_cliente = data['Distancia de voo']

# Calcular as medidas de tendência central
media = np.mean(tipo_cliente)
mediana = np.median(tipo_cliente)
moda = tipo_cliente.mode()[0]

# Calcular as medidas de dispersão
desvio_padrao = np.std(tipo_cliente)
variancia = np.var(tipo_cliente)
amplitude = np.max(tipo_cliente) - np.min(tipo_cliente)

# Calcular as medidas de posição relativa
quartil_25 = np.percentile(tipo_cliente, 25)
quartil_50 = np.percentile(tipo_cliente, 50)
quartil_75 = np.percentile(tipo_cliente, 75)

# Calcular a associação com outro atributo (exemplo: "Tipo de viagem")
tipo_viagem = data['Horario de chegada ou partida']
correlacao = tipo_cliente.corr(tipo_viagem)

# Criar a tabela com as medidas calculadas
tabela = pd.DataFrame({
    'Medidas': ['Média', 'Mediana', 'Moda', 'Desvio Padrão', 'Variância', 'Amplitude', '25º Quartil', '50º Quartil', '75º Quartil', 'Correlação'],
    'Valores': [media, mediana, moda, desvio_padrao, variancia, amplitude, quartil_25, quartil_50, quartil_75, correlacao]
})

# Plotar a tabela
fig, ax = plt.subplots()
ax.axis('off')
ax.table(cellText=tabela.values, colLabels=tabela.columns, loc='center')

# Exibir a tabela plotada
plt.show()
