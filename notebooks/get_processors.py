from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

import pandas as pd

def find_processes(driver):
  driver.get('https://www.solotodo.cl/notebook_processors?id=1326895')
  wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
  processes = []
  for _ in range(1, 11): # 10 páginas
    # Obtener los procesadores
    processes_elements = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div/div/div[4]/div/div/div[1]/div[3]/div')))
    for process_element in processes_elements:
      process = {
        'name': process_element.find_element(By.XPATH,'.//div/div[1]/a').text,
        'score': process_element.find_element(By.XPATH,'.//div/div[6]/span').text,
        'process_url': process_element.find_element(By.XPATH,'.//div/div[1]/a').get_attribute('href')
      }
      processes.append(process)

    # Cambiar la pagina
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div/div/div[4]/div/div/div[2]/div/div[3]/button')))
    button.click()

  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de procesadores
  df = pd.DataFrame(processes)
  df.to_csv('notebooks/processes.csv')