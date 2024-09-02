from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(r'C:\Users\caris\OneDrive\Área de Trabalho\AutoWebLogin')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[1]').send_keys('eli@teste.com')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[2]').send_keys('12345678')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/a/button').click()
sleep(1)

navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[1]').send_keys('Elizangela Caris')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[2]').send_keys('Tatuapé')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[3]').send_keys('São Paulo')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/div/input[4]').send_keys('Brasil')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="download"]').click()

sleep(5)
