import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Selecionar o atributo "Entretenimento a bordo"
entretenimento_bordo = data['Entretenimento a bordo']

# Calcular as frequências dos valores
frequencias = entretenimento_bordo.value_counts().sort_index()

# Calcular a frequência cumulativa em porcentagem
frequencia_cumulativa_percent = frequencias.cumsum() / frequencias.sum() * 100

# Criar os pontos para o gráfico de Ogiva
x = frequencia_cumulativa_percent.index
y = frequencia_cumulativa_percent.values

# Plotar a Ogiva
plt.plot(x, y, linestyle='-', marker='o')

# Configurar os rótulos dos eixos
plt.xlabel('Nível de Satisfação de Entretenimento a bordo')
plt.ylabel('Frequência Cumulativa (%)')

# Configurar o título do gráfico
plt.title('Ogiva - Nível de Satisfação de Entretenimento a bordo')

# Exibir o gráfico
plt.show()
