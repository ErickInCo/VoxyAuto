from cgitb import reset
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException


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
driver.get('https://app.voxy.com/v2/#/home')

WebDriverWait(driver, 25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#login_form_email_input_field')))\
    .send_keys('elerick96@gmail.com')

WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#login_form_submit_button")))\
    .click()

# ?password_input_field
WebDriverWait(driver, 25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#password_input_field')))\
    .send_keys('N@tsuD96')

# voxy-auth-form__submit voxy-button voxy-button_size_l voxy-button_view_primary
WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.voxy-auth-form__submit.voxy-button.voxy-button_size_l.voxy-button_view_primary")))\
    .click()

# unit_lesson_start
# ---------------------------------------------------------------Seleccionar Primera actividad-----------------------------------------------
# Seleccionar la actividad
WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#unit_lesson_start")))\
    .click()



# Iniciar actividad
# ---------------------------------------------------------------Iniciar Leccion-----------------------------------------------
# practice-button btn btn-primary btn-large theme-primary-button
# start-button btn btn-primary btn-large theme-primary-button
try:
    WebDriverWait(driver,5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.practice-button.btn.btn-primary.btn-large.theme-primary-button")))\
        .click()
except TimeoutException:
    print("Error de tiempo o no hay boton")


# Identificar la actividad
# <div class="mode"> Listening Activity</div>

# driver.find_element(By.CSS_SELECTOR, '[name="q"]')
WebDriverWait(driver,25)\
    .until(EC.element_to_be_clickable((By.CLASS_NAME,'name-wrap')))\
    .click()
nombre= driver.find_element(By.CLASS_NAME,'name-wrap')
tActividad=nombre.find_element(By.CSS_SELECTOR,'div[class="mode"]')
# tActividad=driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]')
tActividad= tActividad.text
print(tActividad)
t2Actividad=nombre.find_element(By.CSS_SELECTOR,'div[class="name"]')
t2Actividad= t2Actividad.text
print(t2Actividad)

# ---------------------------------------------------------------Identificar actividad a realizar-----------------------------------------------
if (tActividad=="LISTENING ACTIVITY"):
    t2Actividad=nombre.find_element(By.CSS_SELECTOR,'div[class="name"]')
    t2Actividad= t2Actividad.text
    print(t2Actividad)
    if (t2Actividad=="Hear Me Out"): #checado 2
        # Iniciar la actividad
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        
        
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total)+ "  "+str(x))
            if actual==x:
                try:
                    WebDriverWait(driver,25)\
                        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[data-correctness="true"]')))\
                        .click()
                except ElementClickInterceptedException:
                    pass
                actual2=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
                actual2=actual2.text
                try:
                    actual2=int(actual2)
                except ValueError:
                    actual2=total
                    x=total+1
                finally:
                    actual2=actual
            if actual2!=actual:
                x+=1
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        finally:
            pass
        print(t2Actividad)

    elif (t2Actividad=="Soundbite"): #checado
         # ol path
        # //*[@id="content"]/div[3]/div/div[2]/div/div[2]/ol
        # Iniciar la actividad
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
                .click()
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span[class="total"]')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element(By.CSS_SELECTOR,'span[class="total"]')
        # total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total))
            if actual==x:
                resultados = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div[2]/ol')
                primer = resultados.find_elements(By.TAG_NAME,'li')
                for e in primer:
                    if e.get_attribute('innerHTML').find("distractor_") ==-1:
                        inicio=e.get_attribute('innerHTML').find('d="')
                        fin=e.get_attribute('innerHTML')[inicio+3:].find('"')
                        idbuscar=e.get_attribute('innerHTML')[inicio+3:inicio+3+fin]
                        # print(idbuscar)
                        b='a[data-answer-id="'+idbuscar+'"]'
                        # print(b)
                        # WebDriverWait(driver,25)\
                        #     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,b)))\
                        #     .click()
                        action = ActionChains(driver)
                        source= e.find_element(By.CSS_SELECTOR,b)
                        try:
                            action.double_click(source).perform()
                        except ElementNotInteractableException:
                            print(b)
                        
                x+=1
            else:
                print("No avanza")
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        finally:
            pass
        print(t2Actividad)
        
    elif (t2Actividad=="Watch And Learn"): #checado 2

        # Iniciar la actividad
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.video-quiz-question.displayed.active')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total)+ "  "+str(x))
            if actual==x:
                try:
                    WebDriverWait(driver,25)\
                        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[data-correctness="true"]')))\
                        .click()
                except StaleElementReferenceException:
                    pass
                finally:
                    pass
                actual2=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
                actual2=actual2.text
                try:
                    actual2=int(actual2)
                except ValueError:
                    actual2=total
                    x=total+1
                finally:
                    actual2=actual
            if actual2!=actual:
                x+=1
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        except TimeoutException:
            pass
        finally:
            pass
        
        print(t2Actividad)
    else:
        print("No supe que sub actividad")

elif (t2Actividad=="Déjà Vu"): #checado 3
    # dejavu 
    # Esperar a que salga <div class="word">
    # Obtener los 3 o 4 contenedores \/
    #   div resource-module span7 resource-poi transcript-mode media-hidden
    # Ciclo dar click a todos hasta avanzar
    # <div class="resource-module span7 resource-video transcript-mode media-hidden"><div id="card_57df3a59847f7b601857a199" class="flipable start span4 card"><div class="card-wrapper theme-memory-card-wrapper"><figure class="front"></figure><figure class="back"><h3>vitamin</h3></figure></div></div><div id="card_53bee4c872dd686c377f55ac" class="flipable start span4 card"><div class="card-wrapper theme-memory-card-wrapper"><figure class="front"></figure><figure class="back"><h3>doctor</h3></figure></div></div><div id="card_57e02c70847f7b601d57a19a" class="flipable start span4 card"><div class="card-wrapper theme-memory-card-wrapper"><figure class="front"></figure><figure class="back"><h3>supplement</h3></figure></div></div><div id="card_57b3830b847f7b29788b169b" class="flipable start span4 card"><div class="card-wrapper theme-memory-card-wrapper"><figure class="front"></figure><figure class="back"><h3>need</h3></figure></div></div></div>
    #   div flipable start span4 card
    # Iniciar la actividad
    WebDriverWait(driver,25)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
        .click()
    # Esperar a que esten disponibles los elementos
    WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.word')))\
            .click()
    # Obtener el total de preguntas
    total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
    total=total.text
    total=int(total)
    print(total)
    # Ciclar hasta terminar las preguntas
    x=1
    while x <= total:
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
            .click()
        actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
        actual=actual.text
        actual=int(actual)
        print(str(actual)+" / "+str(total))
        if actual==x:
            resultados = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[1]')
            # flipable start span4 card
            primer = resultados.find_elements(By.CSS_SELECTOR,'div.flipable.start.span4.card')
            for e in primer:
                WebDriverWait(driver,25)\
                    .until(EC.element_to_be_clickable(e))\
                    .click()
            # WebDriverWait(driver,25)\
            #     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[data-correctness="true"]')))\
            #     .click()
            x+=1
        else:
            x-=1

    try:
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
            .click()
    except TimeoutException:
            pass
    finally:
        pass
    print(tActividad)

elif (tActividad=="What Is It?" or t2Actividad=="What Is It?"): #checado 1
    # //*[@id="content"]/div[3]/div/div[2]/div/div[2]/div[1]/ol
    # Iniciar la actividad
    WebDriverWait(driver,25)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
        .click()
    # Esperar a que esten disponibles los elementos
    WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
            .click()
    # Obtener el total de preguntas
    WebDriverWait(driver,25)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span[class="total"]')))\
        .click()
    total=driver.find_element(By.CSS_SELECTOR,'span[class="total"]')
    # total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
    total=total.text
    total=int(total)
    # print(total)
    # Ciclar hasta terminar las preguntas
    x=1
    while x <= total:
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
            .click()
        actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
        actual=actual.text
        actual=int(actual)
        print(str(actual)+" / "+str(total)+ "  "+str(x))
        if actual==x:
            # resultados = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div[2]/div[1]/ol')
            resultados = driver.find_element_by_css_selector('div.word.hide[style="display: block;"]')
            
            primer = resultados.find_elements(By.TAG_NAME,'li')
            ban=0
            for e in primer:
                if e.get_attribute('innerHTML').find("distractor_") ==-1:
                    inicio=e.get_attribute('innerHTML').find('d="')
                    fin=e.get_attribute('innerHTML')[inicio+3:].find('"')
                    idbuscar=e.get_attribute('innerHTML')[inicio+3:inicio+3+fin]

                    b='a[data-answer-id="'+idbuscar+'"]'
                    
                    action = ActionChains(driver)
                    source= e.find_element(By.CSS_SELECTOR,b)
                    try:
                        action.double_click(source).perform()
                    except ElementNotInteractableException:
                        print(b)
            actual2=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual2=actual2.text
            try:
                actual2=int(actual2)
            except ValueError:
                actual2=total
                x=total+1
            finally:
                actual2=actual     
            x+=1        
        else:
            print("No avanza")
            
            
    try:
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
            .click()
    except TimeoutException:
        pass
    finally:
        pass
    print(tActividad)
elif (tActividad=="READING ACTIVITY"):
    
    t2Actividad=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]')
    t2Actividad= t2Actividad.text
    print(t2Actividad)
    if (t2Actividad=="Mind The Gap"): #checado 3
        # ol path
        # //*[@id="content"]/div[3]/div/div[2]/div/div[2]/ol
        # Iniciar la actividad
        # start-button btn btn-primary btn-large theme-primary-button
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total))
            if actual==x:
                resultados = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/ol')
                primer = resultados.find_elements(By.TAG_NAME,'li')
                for e in primer:
                    if e.get_attribute('innerHTML').find("distractor_") ==-1:
                        inicio=e.get_attribute('innerHTML').find('d="')
                        fin=e.get_attribute('innerHTML')[inicio+3:].find('"')
                        idbuscar=e.get_attribute('innerHTML')[inicio+3:inicio+3+fin]
                        print(idbuscar)
                        buscarElemento='a['+idbuscar+'"]'
                        b='a[data-answer-id="'+idbuscar+'"]'
                        action = ActionChains(driver)
                        source= e.find_element(By.CSS_SELECTOR,b)
                        try:
                            action.double_click(source).perform()
                        except ElementNotInteractableException:
                            print(b)
                x+=1
            else:
                print("No avanza")
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        except TimeoutException:
            pass
        finally:
            pass
        print(t2Actividad)
    elif (t2Actividad=="Read Out"): #checado
        # Iniciar la actividad
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total)+ "  "+str(x))
            if actual==x:
                try:
                    WebDriverWait(driver,25)\
                        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[data-correctness="true"]')))\
                        .click()
                except StaleElementReferenceException:
                    pass
                actual2=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
                actual2=actual2.text
                try:
                    actual2=int(actual2)
                except ValueError:
                    actual2=total
                    x=total+1
                finally:
                    actual2=actual
            if actual2!=actual:
                x+=1
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        finally:
            pass
        print(t2Actividad)
    else:
        print("No se que subactivida es")
elif (tActividad=="Picture Perfect" or t2Actividad=="Picture Perfect"):
    print(t2Actividad)
    x = input()
elif (tActividad=="Spellbreaker"):
    print(tActividad)
    x = input()
elif (tActividad.find("Grammar")!=-1 or t2Actividad=="Fragmentstein"): #checado
    print(tActividad)
    # x = input()
    t2Actividad=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]')
    t2Actividad= t2Actividad.text
    print(t2Actividad)
    if (t2Actividad=="Fragmentstein"):
        # ol path
        # //*[@id="content"]/div[3]/div/div[2]/div/div[2]/ol
        # Iniciar la actividad
        # start-button btn btn-primary btn-large theme-primary-button
        WebDriverWait(driver,25)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.start-button.btn.btn-primary.btn-large.theme-primary-button")))\
            .click()
        # Esperar a que esten disponibles los elementos
        WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[style="display: block;"]')))\
                .click()
        # Obtener el total de preguntas
        total=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[2]')
        total=total.text
        total=int(total)
        print(total)
        # Ciclar hasta terminar las preguntas
        x=1
        while x <= total:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.current')))\
                .click()
            actual=driver.find_element_by_xpath('//*[@id="footer"]/div/div/div[3]/div/span[1]')
            actual=actual.text
            actual=int(actual)
            print(str(actual)+" / "+str(total))
            if actual==x:
                resultados = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[2]/ol')
                primer = resultados.find_elements(By.TAG_NAME,'li')
                for e in primer:
                    if e.get_attribute('innerHTML').find("distractor_") ==-1:
                        inicio=e.get_attribute('innerHTML').find('d="')
                        fin=e.get_attribute('innerHTML')[inicio+3:].find('"')
                        idbuscar=e.get_attribute('innerHTML')[inicio+3:inicio+3+fin]
                        print(idbuscar)
                        buscarElemento='a['+idbuscar+'"]'
                        b='a[data-answer-id="'+idbuscar+'"]'
                        action = ActionChains(driver)
                        source= e.find_element(By.CSS_SELECTOR,b)
                        try:
                            action.double_click(source).perform()
                        except ElementNotInteractableException:
                            print(b)
                x+=1
            else:
                print("No avanza")
        try:
            WebDriverWait(driver,25)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.next-button.btn.btn-primary.btn-large.hide.btn-shimmer.theme-primary-button.footer-right-side")))\
                .click()
        except TimeoutException:
            pass
        finally:
            pass
        print(t2Actividad)
    


print("termino")
# 

# -------------------------------------Lista de actiuvidades
# LISTENING ACTIVITY/Hear Me Out
# LISTENING ACTIVITY/Soundbite
# LISTENING ACTIVITY/Watch and Learn
# Déjà vu
# What is it?
# Spellbreaker
# Reading activity/Mind The Gap id
# Reading activity/Read Out  true

# Identificar por Fragmenstein
# Grammar Activity/Fragmentstein  id
# <div class="mode"> Grammar Activity </div>



# ---------------------------------------Botones
# Boton siguiente actividad
# button next-button btn btn-primary btn-large hide btn-shimmer theme-primary-button footer-right-side

# Boton final de leccion
# button cont-button btn btn-primary btn-large footer-right-side hide theme-primary-button theme-primary-button

# Identificar cuando se acabo la leccion
# //*[@id="header"]/div/div/div[2]/div/div/div/div[3]/div/div[2] 
# div.styile width 100
# <div class="bar" style="width: 100%;"></div>



# dejavu 
# Esperar a que salga <div class="word">
# Obtener los 3 o 4 contenedores \/
#   div resource-module span7 resource-poi transcript-mode media-hidden
# Ciclo dar click a todos hasta avanzar
#   div flipable start span4 card















# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
#     .click()

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'input#login_form_email_input_field')))\
#     .send_keys('Madrid')

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'i.icon.icon-search')))\
#     .click()

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'i.icon_weather_s.icon.icon-local')))\
#     .click()

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                       '/html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/a')))\
#     .click()


# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                       '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

# texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')
# texto_columnas = texto_columnas.text

# tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

# horas = list()
# temp = list()
# v_viento = list()

# for i in range(0, len(tiempo_hoy), 4):
#     horas.append(tiempo_hoy[i])
#     temp.append(tiempo_hoy[i+1])
#     v_viento.append(tiempo_hoy[i+2])

# df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'V_viento(km_h)':v_viento})
# print(df)
# df.to_csv('tiempo_hoy.csv', index=False)

# driver.quit()