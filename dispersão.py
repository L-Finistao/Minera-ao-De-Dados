import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv(".\PreProcessamentoMod\codigos\dataPTFiltrado300.csv")

# Define as colunas que serão usadas no diagrama de dispersão
col_age = df['Idade']
col_class = df['Distancia de voo']

# Define as configurações do diagrama de dispersão
plt.scatter(col_age, col_class)

# Adiciona o título e rótulos dos eixos do diagrama de dispersão
plt.title('Diagrama de Dispersão de Idade vs. Distancia')
plt.xlabel('Idade')
plt.ylabel('Distancia')

# Mostra o diagrama de dispersão
plt.show()
