from flask import Flask, render_template

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():


  return render_template('index.html')

def find_notebooks():
  df = pd.read_csv('processes.csv')
  notebooks = []
  for _, row in df.iterrows():
    driver = webdriver.Chrome('/bin/chromedriver')
    driver.get(row['process_url'])
    time.sleep(1)
    notes = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for idx, _ in enumerate(notes, start=1):
      notebook = {
        'name': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/h3/a')[0].text,
        'process': row['name'],
        'score': row['score'],
        'price': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/div[3]/div/a')[0].text,
        'ram': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/div[2]/dl/dd[2]')[0].text,
        'screen': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/div[2]/dl/dd[3]')[0].text,
        'storage': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/div[2]/dl/dd[4]/ul/li')[0].text,
        'link': driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div['+str(idx)+']/h3/a')[0].get_attribute('href'),

      }
      print(notebook)
      notebooks.append(notebook)

    # Cerrar el navegador falso
    driver.quit()

    print(len(notebooks))

  # Guardar la lista de notebooks
  df_notebooks = pd.DataFrame(notebooks)
  df_notebooks.to_csv('notebooks.csv')


def find_processes():
  driver = webdriver.Chrome('/bin/chromedriver')
  driver.get('https://www.solotodo.cl/notebook_processors?id=1326895')
  # Esperar 10 segundos
  # driver.implicitly_wait(10)
  wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

  processes = []
  for _ in range(1, 11): # 10 páginas
    time.sleep(2)
    for i in range(1, 16):
      # Obtener los procesos
      process_element = driver.find_elements_by_xpath('//*[@id="main-container"]/div/div/div[4]/div/div/div[1]/div[3]/div['+str(i)+']/div/div[1]/a')
      process = {
        'name': process_element[0].text,
        'score': driver.find_elements_by_xpath('//*[@id="main-container"]/div/div/div[4]/div/div/div[1]/div[3]/div['+str(i)+']/div/div[6]/span')[0].text,
        'process_url': process_element[0].get_attribute('href')
      }
      processes.append(process)

    # Cambiar la pagina
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div/div/div[4]/div/div/div[2]/div/div[3]/button')))
    button.click()


  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de procesadores
  df = pd.DataFrame(processes)
  df.to_csv('processes.csv')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)