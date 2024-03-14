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

#Coletando os preços dos produtos
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

# inserir os titulos e preços na planilha
for titulo, precos in zip(titulos, precos):
    pass
