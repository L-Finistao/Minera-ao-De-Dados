import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Carregar os dados
data = pd.read_csv("./Database.csv")

# Selecionar atributos e rótulos
atributos = ["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo",
             "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online", "Portao embarque",
             "Comida e bebida", "Embarque online", "Conforto do assento", "Entretenimento a bordo",
             "Servico de bordo", "Conforto nas pernas", "Bagagem de mão", "Check-in", "Servico de voo",
             "Limpeza", "Atraso na partida", "Atraso na chegada"]
rotulo = "Satisfacao"

X = data[atributos]
y = data[rotulo]

# Transformar rótulos categóricos em valores numéricos
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Dividir os dados em conjunto de treinamento e conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Criar e treinar o modelo SVM
model = SVC()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)
