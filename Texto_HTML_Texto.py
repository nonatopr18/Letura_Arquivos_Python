# Retirar só o texto da página da internet
from nltk.tag import TrigramTagger
from nltk.tag import BigramTagger
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import unicodedata
import sys
import nltk
# nltk.download()
from nltk.tokenize import word_tokenize  # Token palavras
from nltk.tokenize import sent_tokenize  # Token frase
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk import word_tokenize
from sklearn.preprocessing import MultiLabelBinarizer
# nltk.download('punkt_tab')
# Gerando um código HTML
html = """
<div class='full_name'><span style='font-weight:bold'>Masego</span> Azra</div>"
"""
# Analisar o HTML
soup = BeautifulSoup(html, "lxml")
# Encontrar o div com a classe full name para mostrar o texto
# print(soup.find("div",{"class" : "full_name"}).text)
# Removendo a pontuação
# Gerando o texto
texto_data = ['Estudar ciência de dados??????, para !!!!!! entender @@@@@  e criar modelos ?????? para datascience???????hoje',
              'Tem-se dois caminhos%%%%%%%%%%%% estudar os modelos teoricos!!!!!!!!!',
              '#########e implementa-los em Python']
# Criando o dicionário para pontuação e caracteres
pontuacao = dict.fromkeys(i for i in range(sys.maxunicode)
                          # o P é para remover pontuação
                          if unicodedata.category(chr(i)).startswith('P'))
texto_tira_pontua = [palavra.translate(pontuacao) for palavra in texto_data]
print(texto_tira_pontua)
# Gerando o texto para tokentizar
texo_imput = "A ciência de dados é uma tecnologia que se usa todos os dias"
# Tokentizando o texto
# Importante: Inicialmente deve-se usar nltk.download(), irá abrir uma
# janela e lá baixar todas as bibliotecas
print(word_tokenize(texo_imput))
# Agora iremos tokenzar por frase
texto_imput2 = " A ciência de dados é a tecnologia do amanhã. O amanhã é hoje."
print(sent_tokenize(texto_imput2))
# Removendo palavras comuns muito repetidas
token_palavras_ingles = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and',
                         'park']
# Carregando o dicionario de acordo com a lingua
palavras_repetidas = stopwords.words('english')
# Removendo as palavras repetidas e comuns
print(token_palavras_ingles)
print([palavras for palavras in token_palavras_ingles if palavras not in palavras_repetidas])
# usando o dicionario de portuges
# note que as palavras tokenzadas devem serem caixa baixa
token_palavra_portugues = ['eu', 'estou', 'indo', 'ali',
                           'vamos', 'e', 'na', 'loja', 'e', 'parque']
repete_palavra_portugues = stopwords.words('portuguese')
print(token_palavra_portugues)
print([palav for palav in token_palavra_portugues if palav not in repete_palavra_portugues])
# Processo inverso, ou seja, voltar a palavra tokenzada
# as palavras originais
# Criando o stemmer
porter = PorterStemmer()
print([porter.stem(palavra) for palavra in token_palavras_ingles])
print([porter.stem(palavra) for palavra in token_palavra_portugues])
# Gerando o texto
texto_dado_ingles = "Chris loved outdoor running"
texto_dado_Portugues = "Barbar ama ver cartazes correndo"
# Usando o modelo pré-treinado
texto_marcado_inlges = pos_tag(word_tokenize(texto_dado_ingles))
texto_marcado_portugues = pos_tag(word_tokenize(texto_dado_Portugues))
print(texto_marcado_inlges)
print(texto_marcado_portugues)
# Gerando o texto para poder indicar
# uma característica no texto
# Texto para ser analisado
tweets = ["I am eating a burrito for breakfast",
          "Political science is an amazing field",
          "San Francisco is an awesome city"]
# Criando a lista com target vazio
marca_tweets = []
# Marcando a palavra em cada tweet
for tweet in tweets:
    tweet_marca = nltk.pos_tag(word_tokenize(tweet))
    marca_tweets.append([marca for palavra, marca in tweet_marca])
# Transformando a marcação em recurso e Usando um modelo
# Terinado do nltk
one_hot_mult = MultiLabelBinarizer()
f_indica = one_hot_mult.fit_transform(marca_tweets)
print(tweets)
print(f_indica)
print(one_hot_mult.classes_) # vendo as classes marcadas
# Treinando o próprio modelo
# Nesse caso observe que estou chamando as bibliotecas
# No meio do código por que iremos trabalhar com um
# Corpo de texto especifico
# Importando as Bibliotecas
# Pegando algums corpos de texto treinado no brown
setencas = brown.tagged_sents(categories='news')
print(setencas) # desabilite se deseja ver as setenças
# Dividindo o conjunto de stenças: 4000 para treino
# 623 para teste
treino = setencas[:4000]
teste = setencas[4000:]
print(treino) # Habilite se deseja ver o conjunto de treino
print(teste) # Habilite se deseja ver o corpus de teste
# Criar a etiqueta de recuo
unigram = UnigramTagger(treino)
bigram = BigramTagger(treino, backoff=unigram)
trigram = TrigramTagger(treino, backoff=bigram)
# Verificando a acuracia
acuracia = trigram.accuracy(teste)
print(f"{acuracia*100:.2f}")  # Acuracia em %
