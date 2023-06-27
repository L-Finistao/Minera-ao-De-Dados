from sklearn.preprocessing import StandardScaler
import pandas as pd

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('./DataBase.csv')

# Extrai a coluna "Satisfacao"
satisfacao = df.pop('Satisfacao')

# Realiza a normalização Z-score dos dados com o StandardScaler
scaler = StandardScaler()
df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Adiciona novamente a coluna "Satisfacao"
df_norm['Satisfacao'] = satisfacao

# Salva o dataframe normalizado em um novo arquivo CSV
df_norm.to_csv('dataPT_norm_zs.csv', index=False)
