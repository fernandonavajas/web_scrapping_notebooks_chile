from flask import Flask, render_template

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time


import pandas as pd

app = Flask(__name__)




@app.route('/')
def index():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  driver = webdriver.Chrome(executable_path='/bin/chromedriver', options=chrome_options)
  find_notebooks(driver)
  return render_template('index.html')

def find_notebooks(driver):
  df = pd.read_csv('processes.csv')
  n_processes = len(df.index)
  n = 0
  notebooks = []
  for _, row in df.iterrows():
    driver.get(row['process_url'])
    time.sleep(1)
    notes_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for note_element in notes_elements:
      notebook = {
        'name': note_element.find_element_by_xpath('.//h3/a').text,
        'process': row['name'],
        'score': row['score'],
        'price': note_element.find_element_by_xpath('.//div[3]/div/a').text,
        'ram': note_element.find_element_by_xpath('.//div[2]/dl/dd[2]').text,
        'screen': note_element.find_element_by_xpath('.//div[2]/dl/dd[3]').text,
        't video': note_element.find_element_by_xpath('.//div[2]/dl/dd[5]/ul').text,
        'storage': note_element.find_element_by_xpath('.//div[2]/dl/dd[4]/ul').text,
        'link': note_element.find_element_by_xpath('.//h3/a').get_attribute('href'),

      }
      n = n+1
      print(f'{ n*100.0/n_processes } % ')
      notebooks.append(notebook)

  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de notebooks
  df_notebooks = pd.DataFrame(notebooks)
  df_notebooks.to_csv('notebooks.csv')


def find_processes(driver):
  driver.get('https://www.solotodo.cl/notebook_processors?id=1326895')
  wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
  time.sleep(3)
  processes = []
  for _ in range(1, 11): # 10 páginas
    # Obtener los procesadores
    processes_elements = driver.find_elements_by_xpath('//*[@id="main-container"]/div/div/div[4]/div/div/div[1]/div[3]/div')
    for process_element in processes_elements:
      process = {
        'name': process_element.find_element_by_xpath('.//div/div[1]/a').text,
        'score': process_element.find_element_by_xpath('.//div/div[6]/span').text,
        'process_url': process_element.find_element_by_xpath('.//div/div[1]/a').get_attribute('href')
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