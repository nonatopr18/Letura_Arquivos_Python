# Preparação de Data Frames
# Carregamento de Data Sets
import numpy as np
import pandas as pd
import requests  # bilbioteca para dados não estruturados
# import pandavro as pdv
import pymysql
from sqlalchemy import create_engine
from sklearn import datasets  # importando os datasets da biblioteca
import matplotlib.pyplot as plt
# Montando o dicionari para gerar o dataframe
dicionario = {"Nome": ['joao', 'Antonio'],
              "Idade": [23, 50],
              "Dirigi": ['Sim', 'Não']}
df = pd.DataFrame(dicionario)
# Adicionar colunas ao dataframe
df["cor"] = ["branco", "negro"]
print(df)
# Note que no mundo organizacional dificilmente irá construir um dataframe do zero
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df2 = pd.read_csv(url)
print(df2.head(10))
print(df2.shape)
# Gerando as Estatísticas Básicas e o tipo de dados do df2
print(df2.describe())
print(df2.info())
