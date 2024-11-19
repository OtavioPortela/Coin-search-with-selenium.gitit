from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from paises import lista_de_paises
import banco



def buscamoeda(pais):
    dia = datetime.now()
    dia_formatado = dia.strftime('%d/%m/%Y')
    #ocultar busca
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    #acessando o navegador
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options= chrome_options)
    #escolhendo site
    navegador.get('https://www.google.com.br/?hl=pt-BR')
    #realizando a busca
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(f'valor moeda {pais}')
    time.sleep(1)
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)
    time.sleep(1)
    valor = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
    moeda = valor.text
    dados = [pais, moeda]
    return dados

lista = []
for x in lista_de_paises:
    busca_completa = buscamoeda(x)
    lista.append(busca_completa)
    
for pais, valor in lista:
    banco.inserir_pais(pais, valor)
    
banco.visualizar_todos()
