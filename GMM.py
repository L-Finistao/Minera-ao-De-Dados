
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Carregar os dados de entrada
data = pd.read_csv('./DataBase300Ent.csv')  # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo de dados
atributos = ["Reserva online"]
rotulo = "Idade" 

# Filtrar o atributo e rótulo
X = data[atributos].values
y = data[rotulo].values

# Criar o objeto do algoritmo GMM
gmm = GaussianMixture(n_components=2)

# Aplicar o algoritmo aos dados
gmm.fit(X)

# Obter os rótulos dos grupos para cada exemplo
labels = gmm.predict(X)

# Plotar gráfico de dispersão do atributo
plt.scatter(X, y, c=labels, cmap='viridis')
plt.xlabel(atributos[0])
plt.ylabel(rotulo)
plt.title("GMM - Gráfico de Dispersão do Atributo")
plt.show()

# Plotar gráfico de barras para contagem de rótulos
unique_labels, counts = np.unique(labels, return_counts=True)
plt.bar(unique_labels, counts)
plt.xticks(unique_labels)
plt.xlabel("Rótulos")
plt.ylabel("Contagem")
plt.title("GMM - Contagem dos Rótulos")
plt.show()
