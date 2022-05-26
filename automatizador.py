from cgitb import reset
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException

import time

# ---------------------------------------------------------------Iniciar-----------------------------------------------
# Opciones de navegación
options =  webdriver.ChromeOptions()

options.add_argument('--start-maximized')
# options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
# driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
# ---------------------------------------------------------------Iniciar Sesion-----------------------------------------------
driver.get('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/index.jsf?pargobmx=1')

# WebDriverWait(driver, 25)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'input#login_form_email_input_field')))\
#     .send_keys('elerick96@gmail.com')
time.sleep(15)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
# driver.get('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/consultaMasivaCpNombre.jsf?pargobmx=1')

# WebDriverWait(driver,25)\
#     .until(EC.element_to_be_clickable((By.ID,"formMain:j_idt57")))\
#     .click()
# ui-chkbox-box ui-widget ui-corner-all ui-state-default
WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default")))\
    .click()

# formMain:j_idt108
WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.ID,"formMain:j_idt113")))\
    .click()

directorio="""C:/Users/1/Documents/VoxyAuto/ARCHIVOS"""
f =open("ARCHIVOS/nombresdearchivos.txt", encoding="utf-8")
nombres=f.readlines()
for x in nombres:
    a=x[0:11]
    driver.find_element_by_name("uploadFile").send_keys(directorio+"/"+a)
    # validar
    WebDriverWait(driver,25)\
        .until(EC.element_to_be_clickable((By.ID,"validar")))\
        .click()
    driver.execute_script("window.history.go(-1)")
# 

# driver.quit()