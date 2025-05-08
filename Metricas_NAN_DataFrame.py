# Gerando medidas básica
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
# Puxar os Dados
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df = pd.read_csv(url)
# Criar ao dicionário
dicionario = {"Máximo": df['Age'].max(),
              "Mínimo": df['Age'].min(),
              "Somatorio": df['Age'].sum(),
              "Total": df['Age'].count(),
              "Média": df['Age'].mean(),
              "Variância": df['Age'].var(),
              "Desvio-Padrão": df['Age'].std(),
              "Curtose": df['Age'].kurt(),
              "Assimetria": df['Age'].skew(),
              "Erro Padrão da Média": df['Age'].sem(),
              "Moda": df['Age'].mode(),
              "Mediana": df['Age'].median()}
# Gerar o dataframe com as medidas
dicionario = pd.DataFrame(dicionario, index=[0])
dicionario = dicionario.round(2)
print(dicionario)
# Selecionando Valores Único de uma coluna
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df2 = pd.read_csv(url)
print(df2['Sex'].unique())
print(df2['Sex'].value_counts())
print(df2['PClass'].value_counts())
print(df2['PClass'].nunique())
# Trantando os valores ausentes
url2 = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df3 = pd.read_csv(url2)
df4 = df3[df3['Age'].isnull()]
print(df4.head(1))
# Substituir todos os male por NaN
df4['Sex'] = df4['Sex'].replace('male', np.nan)
print(df4.head(6))
# Voltar para a configuração inicial
df4['Sex'] = df4['Sex'].replace(np.nan, 'male')
print(df4.head(6))
# Tratando os valores ausentes, nan etc
df5 = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])
print(df5.head(6))
# Entrar com os valoes nulos
df6 = df5[df5["Age"].isna()]
print(df6.head(1))
df7 = df6.fillna(df5["Age"].mean()).head(1)
print(df7.head(1))
