# Passo 1 - Entrar no sistema da empresa
# Passo 2 - Fazer login
# Passo 3 - Exportar a base de dados
# Passo 4 - Calcular os indicadores
# Passo 5 - Enviar um e-mail para o meu chefe

# Instalações : 
# pip install pyautogui - pip install pandas  
# pip install numpy - pip install openpyxl

# Utilizar a ferramenta pyautogui para automatizar o processo do mouse

import pyautogui
import time
import pandas

# Abrindo o navegador opera para começar a automatização
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)

# Entrando no sistema da empresa
pyautogui.write(
    "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(3)

# Preenchendo o usuário
pyautogui.press("tab")
pyautogui.write("teste")

# Preenchendo a senha
pyautogui.press("tab")
pyautogui.write("123")

# Clicando no botão entrar
pyautogui.press("tab")
pyautogui.press("enter")

# Exportando a base de dados
time.sleep(5)
pyautogui.rightClick(x=395, y=371)
time.sleep(1.5)
pyautogui.click(x=530, y=815)
time.sleep(5)

# Calculando os indicadores
tabela = pandas.read_csv(r"C:\Users\User\Downloads\Compras (1).csv", sep=";")
print(tabela)

tabela['ValorFinal'] = tabela['ValorFinal'].str.replace(',', '.').astype(float)
totalGasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = totalGasto / quantidade

# Enviando um e-mail para o chefe
pyautogui.hotkey("ctrl", "t")
time.sleep(2)
pyautogui.write("https://mail.google.com/")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=130, y=168)
time.sleep(3)
pyautogui.write("franzener.math@gmail.com")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab")
pyautogui.write("Relatório de Compras - Matheus Franzener Hohmann")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("Prezado chefe, o total gasto foi de R$ " + str(totalGasto) + " e a quantidade de produtos foi de " + str(quantidade) + " unidades. O preço médio foi de R$ " + str(preco_medio) + ".")
time.sleep(2)
pyautogui.hotkey("ctrl", "enter")
