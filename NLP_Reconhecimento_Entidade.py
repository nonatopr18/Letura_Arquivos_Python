import pandas as pd
import numpy as np
import spacy
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from transformers import pipeline
# Carregando o pacote Spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Rina quero 1$ para comprar Moretti, na Copy")
# Imprimindo cada entidade
print(doc.ents)
# Imprimino a entidade e o seu rotulo
for entidade in doc.ents:
    print(entidade.text, entidade.label_, sep=",")
# Contando a frequencia de uma palavra no texto
texto_dados = np.array(
    ['I love Brazil. Brazil!', 'Sweden is best', 'Germanybeats both'])
# Criando a matriz de recurso com as palavras do texto
conta_palavras = CountVectorizer()
bag_de_palavras = conta_palavras.fit_transform(texto_dados)
print(bag_de_palavras)
print(bag_de_palavras.toarray())  # Conta palavras para cada observação
# Agora será feito a contagem de palavras por componente do texo
print(conta_palavras.get_feature_names_out())
# Criando a matriz de features para contagem de argumentos
conta_2gram = CountVectorizer(ngram_range=(1, 2),
                              stop_words="english",
                              vocabulary=['brazil'])
bag = conta_2gram.fit_transform(texto_dados)
print(bag.toarray())
print(conta_2gram.vocabulary_)
# Bag de palavras ponderado
# Criando o texto
# Gerando a matrix atraves da tf-idf matriz
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(texto_dados)
print(feature_matrix)
print(tfidf.vocabulary_)
# Usando vetores de palavras para calcular a similaridade de textos
# Gerando uma consulta e tranformando num vetor tf-idf
texto = "Brazil is the best"
vetor = tfidf.transform([texto])
# Calculando a similaridaee por coseno entre
# entre o vetor de input e todos os vetores
similaridade_coseno = linear_kernel(vetor, feature_matrix).flatten()
# Pegando os indices mais relevantes ordenados
relaciona_doc_indices = similaridade_coseno.argsort()[:-10:-1]
print(relaciona_doc_indices)
# imprimendo e mostrando os textos similares e procurando
# # Consultando ao longo do texto e calculando a frequencia
print([(texto_dados[i], similaridade_coseno[i])
      for i in relaciona_doc_indices])
# Captando sentimento para fazer previsão
# Gerando a NLP pipeline para rodar os sentimentos e analises
classifidador = pipeline("sentiment-analysis")
# Classificar algum texto
sentimento1 = classifidador("Dona Nilce gosta de misa")
sentimento2 = classifidador("Dona Nilce vende marmita")
print(sentimento1)
print(sentimento2)
