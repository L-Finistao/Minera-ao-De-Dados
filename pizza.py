import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o arquivo test.csv como um DataFrame do pandas
df = pd.read_csv('.\PreProcessamentoMod\codigos\dataPTFiltrado300.csv')

# criando um gráfico de pizza da coluna Age
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60','60-70', '70-80','80-90']
df['age_group'] = pd.cut(df['Idade'], bins=bins, labels=labels)
counts = df['age_group'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title('Porcentagem de Idade')
plt.show()

# criando um histograma da coluna Age
sns.histplot(data=df, x='Idade', bins=20)
plt.title('Distribuição de Idade')
plt.show()
