from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


navegador = webdriver.Chrome()

navegador.get('https://rpachallenge.com/')

elemento = navegador.find_element(by=BY.XPATH, value = '/html/body/script[3]')

elemento.send_Keys('TESTE')

time.sleep(10)

drive.quit()
