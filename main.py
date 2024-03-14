#Adicionando as biblioteclas
# pip install selenium openpyxl

#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Acessar o site https://www.novaliderinformatica.com.br/computadores
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores')

#Coletando os nomes dos produtos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

#

preco = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")
for valor in preco:
    print(valor.text)