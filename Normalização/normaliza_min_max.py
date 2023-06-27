from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('./DataBase.csv')

# Extrai a coluna "Satisfacao"
satisfacao = df.pop('Satisfacao')

# Realiza a normalização dos dados com o MinMaxScaler
scaler = MinMaxScaler()
df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Adiciona novamente a coluna "Satisfacao"
df_norm['Satisfacao'] = satisfacao

# Salva o dataframe normalizado em um novo arquivo CSV
df_norm.to_csv('database_norm.csv', index=False)
