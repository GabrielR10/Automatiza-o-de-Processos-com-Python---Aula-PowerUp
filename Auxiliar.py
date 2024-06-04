#Aula 1 - PowerUp (Automatização de Tarefas)

"""
CRIANDO A LÓGICA PARA ESCREVER O CÓDIGO

PASSO 1: ENTRAR NO SITE DA EMPRESA
https://dlp.hashtagtreinamentos.com/pythin/intensivao/login

PASSO 2: FAZER LOGIN

PASSO 3: IMPORTAR A BASE DE DADOS

PASSO 4: CADASTRAR 1 PRODUTO

PASSO 5: REPETIR O PROCESSO DE CADASTRO ATÉ ACABAR A BASE DE DADOS

"""

#Código para limpar a saída do vscode

#import os

#os.system('cls' if os.name == 'nt' else 'clear')


#Instalando o pyautogui

pip install pyautogui


import pyautogui
import time

#PEGANDO A POSIÇÃO DO MOUSE
time.sleep(5)
print(pyautogui.position())

"""
 codigo       marca        tipo  categoria  preco_unitario  custo               obs
0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
"""