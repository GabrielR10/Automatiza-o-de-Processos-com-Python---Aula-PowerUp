#Importando as bibliotecas

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2 #determina uma pausa de 2 segundos a cada comando 

#PASSO 1: ENTRAR NO SITE DA EMPRESA

#Abrir o navegador 
pyautogui.press("win") #pressiona  a tecla desejada 
pyautogui.write("Microsoft Edge") #escreve o texto
pyautogui.press("enter")

#Entrar no sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Dar uma pausa na automatização 
time.sleep(1.7) #espera 2 segundos para o próximo comando

#PASSO 2: FAZER LOGIN

pyautogui.click(x=724, y=353, clicks = 1) #comando que clica na área específica da tela
pyautogui.write("emaildeacesso@teste.com.br") #escreve o e-mail de acesso
pyautogui.press("tab") #aperta a tecla tab
pyautogui.write("********") #digita a senha de acesso ao sistema da empresa
pyautogui.press("tab") #aperta a tecla tab
pyautogui.press("enter") #aperta a tecla enter
time.sleep(2) # aguardar 2 segundos para carregar a próxima página 

#PASSO 3: IMPORTAR A BASE DE DADOS

tabela = pd.read_csv("produtos.csv")

print(tabela)

#PASSO 4: CADASTRAR 1 PRODUTO
#PASSO 5: REPETIR O PROCESSO DE CADASTRO ATÉ ACABAR A BASE DE DADOS

#criando um laço de repetição para inserir todas as linhas da tabela:

for linha in tabela.index:
    
    #clicar no campo de código de produto
    pyautogui.click(x=698, y=242)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #clicar no campo de marca de produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #clicar no campo de tipo de produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #clicar no campo de categoria de produto
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #o comando write só entende texto, necessita de conversão para string
    pyautogui.press("tab")

    #clicar no campo de preço unitario de produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) #o comando write só entende texto, necessita de conversão para string
    pyautogui.press("tab")

    #clicar no campo de custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"])) #o comando write só entende texto, necessita de conversão para string
    pyautogui.press("tab")

    #clicar no campo de observação
    obs = tabela.loc[linha, "obs"] #deixando a coluna obs em uma variável

    if not pd.isna(obs): #criando uma condição para escrever somente as linhas que não são vazias
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar o cadastro e subir a página para cadastrar o próximo produto
    pyautogui.press("enter")
    pyautogui.scroll(-600) #abaixa um pouco a tela para ver o produto preenchido    
    pyautogui.scroll(5000) #o número alto já somarca do produto be a tela independente do tamanho
