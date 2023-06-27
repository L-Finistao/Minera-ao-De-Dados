import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Selecionar o atributo "Serviço de Check-in"
atributo = data['Check-in']

# Definir o número de intervalos
num_intervalos = 7

# Gerar o histograma
frequencias, intervalos, _ = plt.hist(atributo, bins=num_intervalos, edgecolor='black')

# Calcular os pontos médios dos intervalos
pontos_medios = (intervalos[:-1] + intervalos[1:]) / 2

# Plotar o polígono de frequências
plt.plot(pontos_medios, frequencias, linestyle='-', marker='o')

# Configurar os rótulos dos eixos
plt.xlabel('Intervalo')
plt.ylabel('Frequência')

# Configurar o título do gráfico
plt.title('Polígono de Frequências - Serviço de Check-in')

# Exibir o gráfico
plt.show()
