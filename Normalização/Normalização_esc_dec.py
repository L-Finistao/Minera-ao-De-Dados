import pandas as pd

# Carregar o arquivo CSV
data = pd.read_csv('./DataBase.csv')

# Lista de atributos para normalização
atributos = ["Genero", "Tipo de cliente", "Idade", "Tipo de viagem", "Classe", "Distancia de voo",
             "Servico wifi a bordo", "Horario de chegada ou partida", "Reserva online",
             "Portao embarque", "Comida e bebida", "Embarque online", "Conforto do assento",
             "Entretenimento a bordo", "Servico de bordo", "Conforto nas pernas", "Bagagem de mão",
             "Check-in", "Servico de voo", "Limpeza", "Atraso na partida", "Atraso na chegada"]

# Aplicar a normalização pelo escalonamento decimal
for atributo in atributos:
    min_value = data[atributo].min()
    max_value = data[atributo].max()
    data[atributo] = (data[atributo] - min_value) / (max_value - min_value)

# Salvar o DataFrame normalizado em um novo arquivo CSV
data.to_csv('DataBase_normalizado_esc.csv', index=False)
