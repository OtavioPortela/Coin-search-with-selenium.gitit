from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def main(pais):
    #Tela oculta
    '''
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    '''


    #buscando drive de forma automatica
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico) # , options= chrome_options

    #entrar no site
    navegador.get('https://www.google.com.br/?hl=pt-BR')

    #buscar elementos
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(f'valor moeda {pais}')
    time.sleep(1)
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)
    time.sleep(1)
    #navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    time.sleep(1)
    valor = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
    moeda = valor.text
    return moeda


if __name__ == '__main__':
    main(pais = 'Inglaterra')