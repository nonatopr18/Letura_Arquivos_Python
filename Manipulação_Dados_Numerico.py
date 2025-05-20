# Manipulação de Dados
# Importar Bibliotecas
import pandas as pd
from sklearn import preprocessing
import matplotlib as plt
import numpy as np
import math as mt
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import FunctionTransformer
# Gerando feature
feature = np.array([[-500.5], [-100.1], [0], [100.1], [900.9]])
# Gerando um scalar
sacalar_MiniMax = preprocessing.MinMaxScaler(feature_range=(0, 1))
sacalar_feature = sacalar_MiniMax.fit_transform(feature)
# Usando transformação standartizada
x0 = np.array([[-1000.1], [-200.1], [500.5], [600.6], [9000.9]])
escalar = preprocessing.StandardScaler()
escalarpadronizado = escalar.fit_transform(x0)
# Padronização robusta
x1 = x0
rob_escalar = preprocessing.RobustScaler()
padroniza_robusto = rob_escalar.fit_transform(x1)
# Normalizando os dados para comprimento unitario
x2 = np.array([[0.5, 0.5],
               [1.1, 3.4],
               [1.5, 20.2],
               [1.63, 34.4],
               [10.9, 3.3]])
normalizar_dados = Normalizer(norm="l2").transform(x2)
normalizar_dados2 = Normalizer(norm="l1").transform(x2)
print(sacalar_feature)
print(escalarpadronizado)
print(padroniza_robusto)
print(normalizar_dados)
print(normalizar_dados2)
print("Soma das Primeiras Observaççoes\ 's Valores:",
      normalizar_dados[0, 0] + normalizar_dados2[0, 1])
# Geração de Polinomios e Interação de Features
# Usar o stickilearning integrado polynomialfeatures
x3 = np.array([[2, 3], [2, 3], [2, 3]])
# Gerando o polinomio com interação d grau dois
intera_polinimio = PolynomialFeatures(degree=2, include_bias=False)
print(intera_polinimio.fit_transform(x3))
# se desejar somente a interação, deve-se seguir conforme abaixo
x4 = x3
intera_polinimio2 = PolynomialFeatures(
    degree=2, interaction_only=True, include_bias=False)
print(intera_polinimio2.fit_transform(x4))
# Transformando as Features
x6 = x4
# Definindo a função


def f1(x: int) -> int:
    return x + 10


# Gerando a transformada
f1_trarnsforma = FunctionTransformer(f1)
print(f1_trarnsforma.transform(x6))
# usando a transformmação pelo aplly
df0 = pd.DataFrame(x6, columns=['Feature1', 'Feature2'])
print(df0)
print(df0.apply(f1))
