# Carregamento de Data Sets
import numpy as np
import pandas as pd
import requests  # bilbioteca para dados não estruturados
# import pandavro as pdv
import pymysql
from sqlalchemy import create_engine
from sklearn import datasets  # importando os datasets da biblioteca
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
# Carregando os conjuntos de dados
dados = datasets.load_digits()
features = dados.data
# Gerando o vetor de marcação
target = dados.target
# Vendo os dados
# print(features[0])
# Vendo a descrição dos dados da biblioteca scikitlearn
# print(dados.DESCR)
# visualizando os dados do blob
# plt.scatter(features[:,20], features[:,10], c=target)
# plt.show()
# importando dados de uma url e vendo os dados
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.csv'
df = pd.read_csv(url)
print(df.head(2))
# Abrindo arquivos .json
url1 = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.json'
df1 = pd.read_json(url1, orient='columns')
print(df1.head(2))
# Abrindo arquivo parquet
url2 = 'https://machine-learning-python-cookbook.s3.amazonaws.com/data.parquet'
df2 = pd.read_parquet(url2)
print(df2.head(2))
# Lendo dados avro
# é necessário importar a biblioteca que é para grandes formato de dados
url3 = 'https://machine-learning-python-cookbook.s3.amazonaws.com/data.avro'
df3 = pdv.read_avro(url3)
print(df3.head(3))
# Extrari dados dos SQL
# inicialmente precisa-se criar a conexão
database_connection = create_engine('sqlite:///sample.db')
# Lendo os dados
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)
print(dataframe.head(2))
# FAzer conexão com o SQL com uma conexão local
# É necessário criar a conecção com o banco de dados
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    db='db',
)
# Lendo a query e gerando o data frame
df5 = pd.read_sql("select * from data", conn)
print(df5.head(2))
# Lendo dados do sheet
# Lendo dados diretamente de uma plhanilha do google
# Lendo a planilha
url6 = "https://docs.google.com/spreadsheets/d/1ehC-9otcAuitqnmWksqt1mOrTRCL38dv0K9UjhwzTOA/export?format=csv"
# puxando a planilha
df6 = pd.read_csv(url6)
print(df6.head(2))
# Acessando o dado pelo S#
s3_uri = "s3://machine-learning-python-cookbook/data.csv"
  Credenciais)
       ACCESS_KEY_ID= "xxxxxxxxxxxxx"
       SECRET_ACCESS_KEY= "xxxxxxxxxxxxxxxx"
       # gerando o data frame a partir do S#
       df7= pd.read_csv(s3_uri, storage_options={
    "key": ACCESS_KEY_ID,
    "secret": SECRET_ACCESS_KEY,
}
)
    print(df7.head(2))
    # Carregando dados não estruturados tais como: imagens, som, etc
    # Puxando os dados de txt
    txt_url = "https://machine-learning-python-cookbook.s3.amazonaws.com/text.txt"
    # Transformando em dataframe
    r = requests.get(txt_url)
    # Lendo o arquivo de texto localmente
    with open('text.txt', 'wb') as f:
    f.write(r.content)
    # Lendo o arquivo
    with open('text.txt', 'r') as f:
    text= f.read()
    print(text)
