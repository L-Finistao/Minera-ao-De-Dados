import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Selecionar o atributo "Idade"
idade = data['Idade']

# Definir os limites dos intervalos de idade
limites = range(0, 101, 25)

# Calcular a contagem de cada faixa etária
contagem_idade = pd.cut(idade, bins=limites).value_counts()

# Configurar as cores para cada faixa etária
cores = ['lightblue', 'lightgreen', 'orange', 'lightpink', 'yellow', 'purple', 'red']

# Plotar o Gráfico de Setores
plt.pie(contagem_idade, labels=contagem_idade.index, colors=cores, autopct='%1.1f%%', startangle=90)

# Configurar o título do gráfico
plt.title('Distribuição de Idade por Intervalo de 25 Anos')

# Exibir o gráfico
plt.show()
