import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Aqui se almacenan los datos del navegador, crea una carpeta e indica su ubicación ("C:Users/User/chrome-data")
chromeDataPath = 'FOLDER_PATH'

# Aquí indica los nicks de los usuarios que quieras seguir
userNicksFollow = ['USER_TAG', 'USER_TAG', 'USER_TAG']


# Configurar uc
options = uc.ChromeOptions()
options.add_argument('--user-data-dir=' + chromeDataPath)

# Instanciar el navegador
driver = uc.Chrome(options=options)

for i, userNickFollow in enumerate(userNicksFollow):
    # ir página
    url = 'https://www.instagram.com/' + userNickFollow
    driver.get(url)

    buttonFollow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(concat( " ", @class, " " ), concat( " ", "_aj1-", " " ))]'))
    )


    # Esperar un tiempo aleatorio entre 8 y 20 segundos
    waiting_time = random.randint(8, 20)
    time.sleep(waiting_time)

    # Hacer scraping con el nick actual
    buttonFollow.click()
    print('Se a seguido a ' + userNickFollow)


    time.sleep(5)

    # Si no es el último nick de la lista, cargar el siguiente nick
    if i < len(userNicksFollow)-1:
        next_url = 'https://www.instagram.com/' + userNicksFollow[i+1]
        driver.execute_script(f"window.location.href='{next_url}'")