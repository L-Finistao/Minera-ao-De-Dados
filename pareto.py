import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Selecionar o atributo "Idade"
idade = data['Idade']

# Definir os intervalos de idade
intervalos = range(0, max(idade) + 1, 20)

# Calcular a frequência dos intervalos
frequencia = pd.cut(idade, bins=intervalos, right=False).value_counts().sort_index()

# Calcular a porcentagem acumulada
porcentagem_acumulada = frequencia.cumsum() / frequencia.sum() * 100

# Ordenar os valores de forma decrescente
frequencia = frequencia.sort_index(ascending=False)
porcentagem_acumulada = porcentagem_acumulada.sort_index(ascending=False)

# Calcular o percentual de cada intervalo em relação ao total
percentual_intervalo = (frequencia / frequencia.sum()) * 100

# Plotar o gráfico de Pareto
fig, ax1 = plt.subplots()

# Gráfico de barras para a frequência
ax1.bar(frequencia.index.astype(str), frequencia.values, color='tab:blue')
ax1.set_ylabel('Frequência', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Gráfico de linha para a porcentagem acumulada
ax2 = ax1.twinx()
ax2.plot(frequencia.index.astype(str), porcentagem_acumulada, color='tab:red', marker='o')
ax2.set_ylabel('Porcentagem Acumulada', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Configurar os rótulos do eixo x
ax1.set_xticklabels(frequencia.index.astype(str), rotation=90)

# Configurar o título do gráfico
plt.title('Gráfico de Pareto - Idade')

# Exibir o gráfico
plt.show()
