from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('./DataBase.csv')

# Separar os atributos e os rótulos
atributos = data[["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo", "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online", "Portao embarque", "Comida e bebida", "Embarque online", "Conforto do assento", "Entretenimento a bordo", "Servico de bordo", "Conforto nas pernas", "Bagagem de mão", "Check-in", "Servico de voo", "Limpeza", "Atraso na partida", "Atraso na chegada"]]
rotulo = data["Satisfacao"]

# Split dos dados - 75% treinamento, 25% teste
X_train, X_test, y_train, y_test = train_test_split(atributos, rotulo, test_size=0.25, random_state=1)

# Criar o classificador de árvore de decisão com limite de 20 folhas
clf = DecisionTreeClassifier(max_leaf_nodes=20)

# Treinar o modelo
clf.fit(X_train, y_train)

# Calcular a acurácia
acuracia = clf.score(X_test, y_test)
print("Acurácia do modelo:", acuracia)

# Plotar a árvore de decisão limitada a 20 folhas
fig = plt.figure(figsize=(12, 8))
_ = tree.plot_tree(clf, 
                   feature_names=atributos.columns,  
                   class_names=["Insatisfeito", "Satisfeito"],
                   filled=True,
                   max_depth=5)

plt.show()
