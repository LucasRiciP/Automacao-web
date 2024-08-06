'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
sleep(1)

barra_busca = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
barra_busca.send_keys('Java')
sleep(3)

botao_busca = driver.find_elements(By.XPATH, '//input[@class="gNO89b"]')
botao_busca[0].click()
sleep(5)
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/')
sleep(3)

barra_busca = driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
barra_busca.send_keys('Rua Ricardo Ometto, 635')
sleep(3)

botao_busca = driver.find_elements(By.XPATH, '//*[@id="searchbox-searchbutton"]/span')
botao_busca[0].click()
sleep(3)

botao_foto = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img')
botao_foto[0].click()
sleep(5)
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/')
sleep(3)

barra_busca = driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
barra_busca.send_keys('Rua Ricardo Ometto, 635')
barra_busca.send_keys(Keys.ENTER)
sleep(3)

botao_foto = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img')
botao_foto[0].click()
sleep(5)
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
sleep(3)

barra_busca = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
barra_busca.send_keys('A')
sleep(1)
barra_busca.send_keys('B')
sleep(1)
barra_busca.send_keys('A')
sleep(1)
barra_busca.send_keys('C')
sleep(1)
barra_busca.send_keys('A')
sleep(1)
barra_busca.send_keys('T')
sleep(1)
barra_busca.send_keys('E')
sleep(1)
barra_busca.send_keys(Keys.ENTER)

sleep(5)
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

pesquisar = input("o que deseja pesquisar: ")
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
sleep(1)
try:
    barra_busca = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
    barra_busca.send_keys(pesquisar)
    barra_busca.send_keys(Keys.ENTER)
    sleep(5)
except NoSuchElementException:
    print('Elemento nao encontrado')
except Exception as e:
    print('Tente novamente mais tarde')
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
sleep(2)

typing = driver.find_element(By.XPATH,'//*[@id="user-name"]')
typing.send_keys('standard_user')
sleep(1)

typing = driver.find_element(By.XPATH,'//*[@id="password"]')
typing.send_keys('secret_sauce')
sleep(1)


typing.send_keys(Keys.ENTER)
sleep(3)

typing = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
typing.click()
sleep(2)

typing = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
typing.click()
sleep(2)

typing = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
typing.click()
sleep(5)

typing = driver.find_element(By.XPATH,'//*[@id="checkout"]')
typing.click()
sleep(2)

typing = driver.find_element(By.XPATH,'//*[@id="first-name"]')
typing.send_keys('Lucas')

typing = driver.find_element(By.XPATH,'//*[@id="last-name"]')
typing.send_keys('rici')

typing = driver.find_element(By.XPATH,'//*[@id="postal-code"]')
typing.send_keys('11326533')
sleep(5)

typing = driver.find_element(By.XPATH,'//*[@id="continue"]')
typing.click()
sleep(2)

typing = driver.find_element(By.XPATH,'//*[@id="finish"]')
typing.click()
sleep(5)




