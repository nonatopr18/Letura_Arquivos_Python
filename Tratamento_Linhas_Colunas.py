# Tratamento de Linhas e Colunas de um DataFrame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Gerando o conjunto de dados
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
# Deleta uma coluna
df = pd.read_csv(url)
df2 = df.drop('Age', axis=1)
# Deletando mais de uma coluna
df3 = df.drop(['Age', 'Sex'], axis=1)
df4 = df.drop(df.columns[1], axis=1)
print(df.columns)
print(df2.columns)
print(df3.columns)
print(df4.columns)
# Deletando Linhas
df5 = df[df['Sex'] != 'male']
print(df5.head(6))
# Pode-se usar o drop também para excluir as linhas , por exemplo
df6 = df[df['Name'] != 'Allison, Miss Helen Loraine']
print(df6.head(2))
# Retirar linhas duplicadas do dataframe
df7 = df.drop_duplicates()
print(df.head(2))
print(df7.head(2))
print("Tabela origial", len(df))
print("Tabela com duplicadas", len(df7))
# verifica-se que naõ houve eliminaão de linhas duplicadas pois, os dataframe as linhas são unicas
# Pode-se verificar usando um subconjunto de dados
df8 = df.drop_duplicates(subset=['Sex'])
print("Tabela com subconjuntos", len(df8))
print(df8)
df9 = df.drop_duplicates(subset=['Sex'], keep='last')
print(df9)
