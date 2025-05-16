# Agrupando As Linhas Por valores
# Pucando as bibliotecas
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import datetime
# Puxando os dados
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
df = pd.read_csv(url)
df1 = df.select_dtypes(include='number')
df2 = df.groupby('Sex')[df1.columns].mean()
df3 = df.groupby('Survived')[df1.columns].count()
# print(df1.head(3),round(2))
# Agrupando por data
# Inicialmente iremos criar um dataframe para poder fazer o agrupmaento
# é necessario informar a periodicidade: D: dias, M: Mês, Y:ano
datas = pd.period_range(start='06/06/2017', periods=100000, freq='D')
df4 = pd.DataFrame(index=datas)  # colocando as datas no dataframe
df4['Vendas'] = np.random.randint(1, 10, 100000)
# Contando as vendas por semana - W
# print(df4.resample('w',label='left').count())
# Agrupamento e Estatísticas
df = pd.read_csv(url)
df1 = df.select_dtypes(include='number')
df6 = df[df1.columns].agg('min')
# print(df6)
# Aplicando a conjunto específicos
df7 = df[df1.columns].agg({"Age": ["mean"], "SexCode": ["min", "max"]})
# print(df7, round(1))
# print(df7.columns)
# Looping sobre uma coluna
# for nome in df['Name'][0:10]:
#    print(nome.upper())  # imprimir os nomes maísuculos
df_1 = pd.read_csv(url)
# Criando a função upper


def uppercase(x):
    return x.upper()


# Aplicando a função
# print(df_1['Name'].apply(uppercase)[0:5])
# Aplicando o apply em grpos específicos para contar por grupo
# print(df.groupby('Sex').apply(lambda x: x.count()))
# Concatenando datarames
data1 = {'id': ['1', '2', '3'], 'primeiro_nome': ['Walmir', 'José', 'Maria'],
         'ultimo_nome': ['Mota', 'Bezerra', 'Mota']}
df_01 = pd.DataFrame(data1, columns=['id', 'primeiro_nome', 'ultimo_nome'])
data2 = {'id': ['4', '5', '6'], 'primeiro_nome': ['Francisco', 'Janaina', 'Michele'],
         'ultimo_nome': ['Sousa', 'castro', 'Alencar']}
df_02 = pd.DataFrame(data2, columns=['id', 'primeiro_nome', 'ultimo_nome'])
# Concatenando os dois dataframe
# Caso queira concatenar pelas colunas usa-se axis=1
df_03 = pd.concat([df_01, df_02], axis=0)
# print(df_03)
# Mesclando dataframes
data3 = {'employed_id': ['1', '2', '3', '4'], 'nome': [
    'Abutre', 'Buzunga', 'Adonisgo', 'Aline']}
df_04 = pd.DataFrame(data3, columns=['employed_id', 'nome'])
data4 = {'employed_id': ['3', '4', '5', '6'], 'venda': [23, 34, 12, 45]}
df_05 = pd.DataFrame(data4, columns=['employed_id', 'venda'])
print(df_04)
print(df_05)
print(pd.merge(df_04, df_05, on='employed_id'))
# Fazendo o merge com todos
print(pd.merge(df_04, df_05, on='employed_id', how='outer'))
# FAzendo o merge com a pimeira coluna
print(pd.merge(df_04, df_05, on='employed_id', how='left'))
# FAzendo o merge com a segunda coluna
print(pd.merge(df_04, df_05, on='employed_id', how='right'))
# é possível escolher a coluna para controle
print(pd.merge(df_04, df_05, left_on = 'employed_id', right_on='employed_id'))