# Detectando Outliers
# Importar Bibliotecas
import pandas as pd
from sklearn import preprocessing
import matplotlib as plt
import numpy as np
import math as mt
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import FunctionTransformer
from sklearn.covariance import EllipticEnvelope
from sklearn.preprocessing import _discretization
from sklearn.datasets import make_blobs
from sklearn.preprocessing import Binarizer
from sklearn.cluster import KMeans
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Criando e simulando dados
features, _ = make_blobs(n_samples=10, n_features=2, centers=1, random_state=1
                         )
# Substituindo os primeiros valores por valores extremos
features[0, 0] = 10000
features[0, 1] = 10000
# Detectando o outlier
detecta_outlier = EllipticEnvelope(
    contamination=.1)  # Considerando 10% de outlier
detecta_outlier.fit(features)  # fitando os outliers
print(detecta_outlier.predict(features))  # Predizendo os outliers
feature = features[:, 0]
print(feature)
# Criando a função para retornar os index dos outliers


def indice_outlier(x: int) -> np.array(int):
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3-q1
    linha_inferior = q1 - (iqr*1.5)
    linha_superior = q3 + (iqr*1.5)
    return np.where((x > linha_inferior) | (x < linha_superior))


print(indice_outlier(feature))
# Trabalhando com outlier
casa = pd.DataFrame()
casa['Preço'] = [534433, 392333, 293222, 4322032]
casa['Banheiros'] = [2, 3.5, 2, 116]
casa['M2'] = [1500, 2500, 1500, 48000]
# Filtrando o dataframe
print(casa[casa['Banheiros'] < 20])
# Gerando o campo outlier
casa["Outlier"] = np.where(casa['Banheiros'] < 20, 0, 1)
casa["log dos M2"] = [np.log(x) for x in casa["M2"]]
print(casa)
# Dicretizando as features
idade = np.array([[6], [12], [20], [36], [65]])
# Definindo o corte
corte = Binarizer(threshold=18)
print(corte.fit_transform(idade))
# Gerando Vários Thresholds
print(np.digitize(idade, bins=[20, 30, 64]))
print(np.digitize(idade, bins=[18]))
# Agrupando Dados Pelos Cluster
f1, _ = make_blobs(n_samples=50, n_features=2, centers=3, random_state=1)
print(f1)
# Gerando o dataframe
df1 = pd.DataFrame(f1, columns=["feature1", "feature2"])
print(df1.head(6))
# Gerando o Agrupamento
cluster = KMeans(3, random_state=0)
# Fitando o cluster
cluster.fit(f1)
# Predizando os valores
df1["Grupo"] = cluster.predict(f1)
print(df1.head(12))
# Deletando valores ausentes, missing ou na
f2 = np.array([[1.1, 11.1],
               [2.2, 22.2],
               [3.3, 33.3],
               [4.4, 44.4],
               [np.nan, 55]])
# excluindo os valores que não interessa
f3 = f2[~np.isnan(f2).any(axis=1)]
print(f3)
# usando o pandas
df4 = pd.DataFrame(f2, columns=["x1", "x2"])
print(df4.dropna())
# Atribuindo Valores Ausentes
f8, _ = make_blobs(n_samples=1000, n_features=2, random_state=1)
# Padronizando as features
padronizacao = StandardScaler()
padroniza_f8 = padronizacao.fit_transform(f8)
# Gerando na para as primeiras features
valor_verdade = padroniza_f8[0, 0]
padroniza_f8[0, 0] = np.nan
# Estimando o valor ausente na matriz
KNN_imputer = KNNImputer(n_neighbors=5)
knn_f8_imputed = KNN_imputer.fit_transform(padroniza_f8)
print("True Value:", valor_verdade)
print("Imputed Value:", knn_f8_imputed[0, 0])
# Estimando pela biblioteca sckitlearn pela média
f9 = f8
# Padronizando as features
padronizacao = StandardScaler()
padroniza_f9 = padronizacao.fit_transform(f9)
# Gerando na para as primeiras features
valor_verdade2 = padroniza_f9[0, 0]
padroniza_f9[0, 0] = np.nan
# Gerando o imputer usand a média como estrategia
mean_imputer = SimpleImputer(strategy="mean")
f9_mean_imputer = mean_imputer.fit_transform(f9)
print("True Value:", valor_verdade2)
print("Imputed Value:", f9_mean_imputer[0, 0])
