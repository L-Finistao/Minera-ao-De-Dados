import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de dados
data = pd.read_csv('./Database.csv')

# Selecionar o atributo "Idade"
idade = data['Idade']

# Calcular a distribuição de frequência
maior_valor = idade.max()
menor_valor = idade.min()
intervalo = (maior_valor - menor_valor) // 15
intervalo = int(intervalo) + 1
frequencia = idade.value_counts(bins=intervalo, sort=False)

# Obter os limites dos intervalos
limites = [intervalo.left for intervalo in frequencia.index]

# Criar os rótulos para os intervalos
rotulos = [f'{int(intervalo.left)} a {int(intervalo.right)}' for intervalo in frequencia.index]

# Obter a quantidade de entidades em cada intervalo
quantidade_entidades = frequencia.values

# Plotar o histograma
plt.bar(rotulos, quantidade_entidades, edgecolor='black')
plt.xlabel('Intervalo de Idade')
plt.ylabel('Quantidade de Pessoas')
plt.title('Faixa Etária dos Passageiros')
plt.xticks(rotation=45)
plt.show()
