#Adicionando as biblioteclas
# pip install selenium openpyxl

#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Acessar o site https://www.novaliderinformatica.com.br/computadores
driver = webdriver.Chrome()
driver.get()