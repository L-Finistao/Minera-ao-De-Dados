import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Mapear os valores categóricos de satisfação para valores numéricos
satisfacao_numerica = data['Satisfacao'].map({'Satisfeito': 1, 'Neutro ou Insatisfeito': 2})

# Selecionar os atributos de interesse
idade = data['Idade']
satisfacao = satisfacao_numerica
quantidade = data.shape[0]  # Obter a quantidade de elementos

# Criar uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar o gráfico de dispersão em 3D
ax.scatter(idade, satisfacao, quantidade)

# Configurar os rótulos dos eixos
ax.set_xlabel('Idade')
ax.set_ylabel('Satisfação')
ax.set_zlabel('Quantidade de Elementos')

# Configurar o título do gráfico
plt.title('Gráfico de Dispersão 3D - Idade x Satisfação x Quantidade de Elementos')

# Exibir o gráfico
plt.show()
