    # Navigate to url
from cgitb import reset
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
options =  webdriver.ChromeOptions()

options.add_argument('--start-maximized')
# options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get("file:///C:/Users/1/Documents/VoxyAuto/Hola.html")

    # Returns TagName of the element
# attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name
# cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')
# valor = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('data-answer-id')


# data-answer-id
resultados = driver.find_element_by_xpath("/html/body/ol")
primer = resultados.find_elements(By.TAG_NAME,'li')
for e in primer:
        if e.get_attribute('innerHTML').find("distractor_") ==-1:
            inicio=e.get_attribute('innerHTML').find('d="')
            fin=e.get_attribute('innerHTML')[inicio+3:].find('"')
            idbuscar=e.get_attribute('innerHTML')[inicio+3:inicio+3+fin]
            print(idbuscar)

