import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

# Carregar os dados
data = pd.read_csv("Database.csv")

# Selecionar atributos e rótulos
atributos = ["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo",
             "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online", "Portao embarque",
             "Comida e bebida", "Embarque online", "Conforto do assento", "Entretenimento a bordo",
             "Servico de bordo", "Conforto nas pernas", "Bagagem de mão", "Check-in", "Servico de voo",
             "Limpeza", "Atraso na partida", "Atraso na chegada"]
rotulo = "Satisfacao"

X = data[atributos]
y = data[rotulo]

# Divisão Holdout (Treinamento 70% e Teste 30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo K-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Calcular a matriz de confusão
confusion = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(confusion)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)

# Calcular o F1 Score
f1 = f1_score(y_test, y_pred, average='weighted')
print("F1 Score:", f1)

# Divisão Cross-Validation (k=10)
y_pred_cv = cross_val_predict(knn, X, y, cv=10)

# Calcular a matriz de confusão (Cross-Validation)
confusion_cv = confusion_matrix(y, y_pred_cv)
print("Matriz de Confusão (Cross-Validation):")
print(confusion_cv)

# Calcular a acurácia (Cross-Validation)
accuracy_cv = accuracy_score(y, y_pred_cv)
print("Acurácia (Cross-Validation):", accuracy_cv)

# Calcular o F1 Score (Cross-Validation)
f1_cv = f1_score(y, y_pred_cv, average='weighted')
print("F1 Score (Cross-Validation):", f1_cv)

# Criar a tabela de resultados
resultados = pd.DataFrame({
    
    "Métrica": ["Acurácia", "F1 Score"],
    "Holdout": [accuracy, f1],
    "Cross-Validation": [accuracy_cv, f1_cv]
})

# Plotar a tabela
plt.figure(figsize=(8, 4))
plt.axis('off')
plt.table(cellText=resultados.values, colLabels=resultados.columns, cellLoc='center', loc='upper left')
plt.title("Resultados dos Classificadores")
plt.show()
