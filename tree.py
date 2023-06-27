import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./DataBase.csv')

# Separar os atributos e os rótulos
atributos = data[["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo", "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online", "Portao embarque", "Comida e bebida", "Embarque online", "Conforto do assento", "Entretenimento a bordo", "Servico de bordo", "Conforto nas pernas", "Bagagem de mão", "Check-in", "Servico de voo", "Limpeza", "Atraso na partida", "Atraso na chegada"]]
rotulo = data["Satisfacao"]

# Codificar os atributos categóricos
le = preprocessing.LabelEncoder()
for coluna in atributos.columns:
    atributos[coluna] = le.fit_transform(atributos[coluna])

# Criar o classificador de árvore de decisão
modelo = DecisionTreeClassifier()

# Treinar o modelo
modelo.fit(atributos, rotulo)

# Exportar a árvore de decisão para visualização
export_graphviz(modelo, out_file='arvore.dot',
                feature_names=atributos.columns,
                class_names=["Insatisfeito", "Satisfeito"],
                filled=True, rounded=True,
                special_characters=True)

# Plotar a árvore de decisão
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.show()
