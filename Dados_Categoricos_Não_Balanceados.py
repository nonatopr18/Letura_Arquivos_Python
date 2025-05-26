# Trabalhando com dados Categorizados não balanceados
# Puando as bibliotecas
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import matplotlib as plt
# Lendo o conjunto de dados da biblioteca
iris = load_iris()
# Gerando as features
features = iris.data
# Gerando as target
target = iris.target
# Desbalancear os dados para isso iremos remover 40 observações
features = features[40:, :]
target = target[40:]
# Criando a classe binaria com o vetor indicador zero
target = np.where((target == 0), 0, 1)
print(target)
# Gerando os pesos para as classes
pesos = {0: .9, 1: .1}
# Gerando o classificador através do classificador random forest
print(RandomForestClassifier(class_weight=pesos))
# Caso queira usar o modelo balanceado o algoritmo usara o peso pelo inverso da frequencia
print(RandomForestClassifier(class_weight='balanced'))
# Ajustando as classes
i_classe0 = np.where(target == 0)[0]
i_classe1 = np.where(target == 1)[0]
# Total de observações em cada classe
n_classe0 = len(i_classe0)
n_classe1 = len(i_classe1)
print(n_classe0)
print(n_classe1)
# Para cada observaçao da classe 0, amostrar aleatoriamente a classe1
i_classe1_reduzida = np.random.choice(i_classe1, size=n_classe0, replace=False)
print(i_classe1_reduzida)
# Juntando a matriz e classe 0 com a matriz subamostrada
print(np.vstack((features[i_classe0, :],
      features[i_classe1_reduzida, :]))[0:5])
# Aumentando a classe 1
i_classe0_aumenta = np.random.choice(i_classe0, size=n_classe1, replace=True)
print(i_classe0_aumenta)
# Juntando a matriz e classe 1 com a matriz subamostrada
print(np.concatenate((target[i_classe0_aumenta], target[i_classe1])))
# Aumentando a classe zero
print(np.vstack((features[i_classe0_aumenta, :], features[i_classe1, :]))[0:5])
