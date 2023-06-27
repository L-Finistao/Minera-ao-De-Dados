import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('.\PreProcessamentoMod\codigos\dataPTFiltrado300.csv')

# Lista com as colunas a serem analisadas
colunas = ['Genero','Tipo de cliente','Idade','Tipo de viagem','Classe','Distancia de voo','Servico wifi a bordo',
'Horario de chegada ou partida','Reserva online','Portao embarque','Comida e bebida','Embarque online',
'Conforto do assento','Entretenimento a bordo','Servico de bordo','Conforto nas pernas','Bagagem de mão',
'Check-in','Servico de voo','Limpeza','Atraso na partida','Atraso na chegada']

# Criação de um dicionário para armazenar os resultados
resultados = {'Colunas': [], 'Media': [], 'Mediana': [], 'Moda': [], 'Desvio Padrão': [], 'Coeficiente de Variação': [], 
              'Primeiro Quartil': [], 'Terceiro Quartil': [], 'Mínimo': [], 'Máximo': [], 'Assimetria': [], 'Curtose': []}

# Loop para calcular as medidas estatísticas para cada coluna
for coluna in colunas:
    resultados['Colunas'].append(coluna)
    resultados['Media'].append(df[coluna].mean())
    resultados['Mediana'].append(df[coluna].median())
    resultados['Moda'].append(df[coluna].mode().values[0])
    resultados['Desvio Padrão'].append(df[coluna].std())
    resultados['Coeficiente de Variação'].append(df[coluna].std() / df[coluna].mean())
    resultados['Primeiro Quartil'].append(df[coluna].quantile(0.25))
    resultados['Terceiro Quartil'].append(df[coluna].quantile(0.75))
    resultados['Mínimo'].append(df[coluna].min())
    resultados['Máximo'].append(df[coluna].max())
    resultados['Assimetria'].append(df[coluna].skew())
    resultados['Curtose'].append(df[coluna].kurtosis())

# Criação do dataframe com os resultados
resultados_df = pd.DataFrame(resultados)

# Impressão dos resultados na tela
print(resultados_df)

# Cálculo da matriz de correlação
matriz_correlacao = df.corr()

# Salva a matriz de correlação no arquivo resultado.txt
with open('resultado.txt', 'w') as f:
    f.write(str(matriz_correlacao))
