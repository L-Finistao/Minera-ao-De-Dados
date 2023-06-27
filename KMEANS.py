from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('./DataBase300Ent.csv')
print(df.describe())

# Extrai a coluna "Satisfacao"
satisfacao = df.pop('Satisfacao')

# Normaliza os dados usando Z-score
scaler = StandardScaler()
df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Aplica o PCA para reduzir a dimensionalidade dos atributos
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df_norm))

# Escolhe o número de clusters desejado para o K-means
k = 5

# Aplica o K-means nos dados reduzidos pelo PCA
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(df_pca)

# Adiciona a coluna de cluster gerada no dataframe
df_pca['Cluster'] = clusters

# Adiciona novamente a coluna "Satisfacao"
df_pca['Satisfacao'] = satisfacao

# Plota o gráfico dos clusters gerados
plt.scatter(df_pca[0], df_pca[1], c=df_pca['Cluster'], cmap='viridis')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title(f'K-means Clustering (k={k})')
plt.show()
