import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# carregar dados
data = pd.read_csv("C:\Users\lukas\Desktop\Mineração\codigos\dataPTFiltrado300.csv")
# selecionar atributos
atributos = ["Genero","Tipo de cliente","Idade","Tipo de viagem","Classe","Distancia de voo","Servico wifi a bordo","Horario de chegada ou partida","Reserva online","Portao embarque","Comida e bebida","Embarque online","Conforto do assento","Entretenimento a bordo","Servico de bordo","Conforto nas pernas","Bagagem de mão","Check-in","Servico de voo","Limpeza","Atraso na partida","Atraso na chegada"]

# separar dados de entrada (X) e rótulos (y)
X = data[atributos].values
y = data["Satisfacao"].values

# normalizar dados de entrada
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# aplicar PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_std)

# plotar gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plotar pontos
for i in np.unique(y):
    ix = np.where(y == i)
    ax.scatter(X_pca[ix, 0], X_pca[ix, 1], X_pca[ix, 2], label=i)

# configurar rótulos dos eixos
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

# configurar título e legenda
ax.set_title('PCA - Dados de Satisfação dos Clientes')
plt.legend()

# exibir gráfico
plt.show()
