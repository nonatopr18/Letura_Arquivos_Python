# Dados Categorizados
# Inicialmente iremos tratar os dados nominais, ou sejam, aqueles que não possuem uma ordenação intriseca
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelBinarizer,MultiLabelBinarizer,label_binarize
from sklearn.feature_extraction import DictVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
# Gerando as features
#classes = ('Fortaleza', 'São Luis', 'Natal', 'Rio Branco', 'São Paulo')
f0 = np.array([["Fortaleza"], ["São Luis"], ["Natal"],
              ["Rio Branco"], ["São Paulo"]])
# Gerando o encoder
rotulos = LabelBinarizer()
print(rotulos.fit_transform(f0))
# Gerando as classes diretamente no vetor
rotulos.classes_
# Para fazer a transformação inversa
print(pd.get_dummies(f0[:,0]))
# Para multiclasses
f0_mult = [("Rio Branco","São Paulo"),
           ("Caracas","Rio de Janeiro"),
           ("Fortaleza","Curitiba"),
           ("Belo Horizonte","Brasilia"),
           ("Rio Branco","Porto Alegre")]
rotulo_mult = MultiLabelBinarizer()
print(rotulo_mult.fit_transform(f0_mult))
print(rotulo_mult.classes)
# Analise de Dados Qualitativos ordinais
df = pd.DataFrame({"Score":["alto","baixo","médio","médio","baixo"]})
# Gerando o mapa codificado
mapa = {"alto":1,"médio":2,"baixo":3}
print(df["Score"].replace(mapa))
# Transformar o dicionário na matriz de recursos
dado_dicionario = [{"Vermelho": 2, "Azul": 4},
{"Vermelho": 4, "Azul": 3},
{"Azul": 1, "Amarelo": 2},
{"Azul": 2, "Amarelo": 2}]
# Gerando o dicionarios vetorizado
vetor_dicionario = DictVectorizer(sparse=False)
# Converter o dicionario em matriz de dados
variaveis = vetor_dicionario.fit_transform(dado_dicionario)
print(variaveis)
nome_variaveis = vetor_dicionario.get_feature_names_out(dado_dicionario)
print(nome_variaveis)
print(pd.DataFrame(variaveis, columns=nome_variaveis))
# Estimar valores ausentes
# Gerando a matriz com dados categoricos
X =np.array([[0, 2.10, 1.45],[1, 1.18, 1.33],[0, 1.22, 1.27],[1, -0.21, -1.19]])
# Gerando a matriz com valores ausentes
X_Valores_nan = np.array([[np.nan, 0.87, 1.31],[np.nan, -0.67, -0.22]]) 
# Treinando o KNN
clf = KNeighborsClassifier(3,weights='distance')
Treina_Modelo = clf.fit(X[:,1:],X[:,0])
# Fazendo a predição do modelo
imputando_valores = Treina_Modelo.predict(X_Valores_nan[:,1:])
# Juntando as matrizes com na e as features
X_junta_imputa = np.hstack((imputando_valores.reshape(-1,1),X_Valores_nan[:,1:]))
# juntando as features numa matrix
print(np.vstack((X_junta_imputa,X)))
# De forma alternativa pode-se preencher os valors de maior frequencia
X_completa = np.vstack((X_Valores_nan,X))
imputa_valor = SimpleImputer(strategy= 'most_frequent')
print(imputa_valor.fit_transform(X_completa))

