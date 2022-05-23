from selenium.webdriver.common.by import By

import pandas as pd

def find_processes(driver):
  print("Searching processes")
  driver.get('https://www.solotodo.cl/notebook_processors?id=1326895')
  processes = []
  for _ in range(1, 6): # 10 páginas
    # Obtener los procesadores
    processes_elements = driver.find_elements_by_xpath('//*[@id="main-container"]/div/div/div[4]/div/div/div[1]/div[3]/div')
    for process_element in processes_elements:
      process = {
        'name': process_element.find_element(By.XPATH,'.//div/div[1]/a').text,
        'score': process_element.find_element(By.XPATH,'.//div/div[6]/span').text,
        'process_url': process_element.find_element(By.XPATH,'.//div/div[1]/a').get_attribute('href')
      }
      processes.append(process)

    # Cambiar la pagina
    button = driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[4]/div/div/div[2]/div/div[3]/button')
    button.click()

  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de procesadores
  df = pd.DataFrame(processes)
  df.to_csv('notebooks/processes.csv')