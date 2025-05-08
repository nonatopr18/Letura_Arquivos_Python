# Fatiando o dataframe
import numpy as np
import pandas as pd
import collections
import requests  # bilbioteca para dados não estruturados
# import pandavro as pdv
import pymysql
from sqlalchemy import create_engine
from sklearn import datasets  # importando os datasets da biblioteca
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
# transformando o csv em data frame
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df = pd.read_csv(url)
# Selecionando as pimeiras linhas
print(df.iloc[2:6])
df = df.set_index(['Name'])
# Fatiando por uma coluna que não seja indice
# print(df.loc['Allen, Miss Elisabeth Walton'])
# Gerando o conjunto de dados por condicionais
url2 = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df2 = pd.read_csv(url2)
print(df2[df2['Sex'] == 'male'].head(5))
# Fazendo uma condicional Dupla
# o head é para imprimir somente as duas primeiras linhas
print(df2[(df2['Sex'] == 'male') & (df2['Age'] >= 65)].head(2))
# Classificar o data frame com base em uma coluna
url3 = url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df3 = pd.read_csv(url3)
print(df3.sort_values(by=['Age']).head(10))
# Substituir Valores Num Data Frame
url5 = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df5 = pd.read_csv(url5)
df6 = df5['Sex'].replace(['female', 'male'], ['Homen', 'Mulher'])
print(df6.head(10))
# Mudando os dados em todo o dataframe
df7 = df5.replace(1, "One")
print(df7.head(10))
df8 = df5.replace("1st", "First", regex=True)
print(df8.head(3))
# Renomeando as Colunas
url9 = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df9 = pd.read_csv(url9)
df10 = df9.rename(columns={'PClass': 'Classe_Passageiro', 'Sex': 'Gênero'})
print(df10.head(1))
# Renomear todas as colunas de uma vez
# Criar o dicionario
nome_colunas = collections.defaultdict(str)
for nome in df10.columns:
    nome_colunas[nome]
print(nome_colunas)
print(df10.head(5))
