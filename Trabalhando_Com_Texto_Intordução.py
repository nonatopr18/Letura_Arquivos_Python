# Iniciando as redes neurais: manipulaçao de textos
import pandas as pd
import sklearn as sk
import numpy as np
import re
# Gerando o text
texto_data = [" Autoridade Kelvin cadê a tese. Rapaz cuida do projeto ",
              "A Janja agora é a chefe de vocês . Vai cortar o ponto dos grevistas",
              " Agora estudar redes neurias com o Bolsonaro. Cuida pede a vaga para mim "]
# Tirando so espaços em branco do texto
tira_espaco_branco = [string.strip() for string in texto_data]
print(texto_data)
print(tira_espaco_branco)
# retirar pontuação
remover_periodos = [string.replace(".", "") for string in tira_espaco_branco]
print(remover_periodos)
# Criando uma função para ajustar qualquer texto em caixa alta


def capitalizer(palavras: str) -> str:
    return palavras.upper()


print([capitalizer(palavras) for palavras in remover_periodos])
# Fazendo operações em strings para mudar o texto
# Gerando a função para trocar letras por XXX


def troca_letra_por_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)


print([troca_letra_por_X(string) for string in remover_periodos])
# Pré processamento de texto
# Definindo a string
S = "Aprendizado de máquina em python livro de aplicacoes"
# Encontrar o primeiro índice da letra
indice_n = S.find("n")
print(indice_n)
# Verificando se a string começa ou não com m
starts_branco_m = S.startswith("m")
print(starts_branco_m)
# Verificar se a string começa ou não com python
fim_branco_python = S.endswith("python")
print(fim_branco_python)
# Verificando se tem alphanumerico
is_alnum = S.isalnum()
print(is_alnum)
# Verificando se é composto por caracteres alfabeticos sem espaço
is_alpha = S.isalpha()
print(is_alpha)
# Verificando o enconde utf-8
uncode_as_utf8 = S.encode("utf-8")
print(uncode_as_utf8)
# Decode utgf-8
decode = uncode_as_utf8.decode("utf-8")
print(decode)
