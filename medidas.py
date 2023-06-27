import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv(".\PreProcessamentoMod\codigos\dataPTFiltrado300.csv")
x = "Idade"
# Define a coluna desejada
coluna = df[x]

# Medidas de tendência central
media = coluna.mean()
mediana = coluna.median()
moda = coluna.mode()[0]

# Medidas de dispersão
variancia = coluna.var()
desvio_padrao = coluna.std()
amplitude = coluna.max() - coluna.min()

# Medidas de posição relativa
percentil_25 = coluna.quantile(0.25)
percentil_50 = coluna.quantile(0.50)
percentil_75 = coluna.quantile(0.75)

# Medidas de associação
#correlacao = coluna.corr(df['Type of Travel'])

# Exibe as medidas calculadas na tela
print("------ ", x, " ------")
print("Medidas de tendência central:")
print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print()
print("Medidas de dispersão:")
print("Variância:", variancia)
print("Desvio padrão:", desvio_padrao)
print("Amplitude:", amplitude)
print()
print("Medidas de posição relativa:")
print("Quantil 25%:", percentil_25)
print("Quantil 50%:", percentil_50)
print("Quantil 75%:", percentil_75)
print()
print("Medidas de associação:")
for col in ['Genero','Tipo de cliente','Idade','Tipo de viagem','Classe','Distancia de voo','Servico wifi a bordo',
'Horario de chegada ou partida','Reserva online','Portao embarque','Comida e bebida','Embarque online',
'Conforto do assento','Entretenimento a bordo','Servico de bordo','Conforto nas pernas','Bagagem de mão',
'Check-in','Servico de voo','Limpeza','Atraso na partida','Atraso na chegada']:
    print(f"Correlação com ",col,":", coluna.corr(df[col]))
