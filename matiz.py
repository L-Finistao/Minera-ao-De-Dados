import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('./Database.csv')

# Selecionar os atributos desejados
atributos = ["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo",
             "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online", "Portao embarque",
             "Comida e bebida", "Embarque online", "Conforto do assento", "Entretenimento a bordo",
             "Servico de bordo", "Conforto nas pernas", "Bagagem de mão", "Check-in", "Servico de voo",
             "Limpeza", "Atraso na partida", "Atraso na chegada"]

# Filtrar os dados apenas pelos atributos selecionados
dados = data[atributos]

# Calcular a matriz de correlação
matriz_correlacao = dados.corr()

# Criar um gráfico de matriz de correlação
fig, ax = plt.subplots(figsize=(12, 10))
im = ax.imshow(matriz_correlacao, cmap='coolwarm')

# Configurar os rótulos dos eixos
ax.set_xticks(np.arange(len(atributos)))
ax.set_yticks(np.arange(len(atributos)))
ax.set_xticklabels(atributos, rotation=45, ha='right')
ax.set_yticklabels(atributos)

# Adicionar os valores da matriz de correlação nas células
for i in range(len(atributos)):
    for j in range(len(atributos)):
        text = ax.text(j, i, f"{matriz_correlacao.iloc[i, j]:.2f}", ha='center', va='center', color='w')

# Configurar o título do gráfico
ax.set_title("Matriz de Correlação")

# Mostrar a barra de cores
plt.colorbar(im)

# Exibir o gráfico
plt.show()
