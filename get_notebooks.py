from selenium.webdriver.support import expected_conditions as EC

import time

import pandas as pd

def find_notebooks(driver):
  df = pd.read_csv('processes.csv')
  n_processes = len(df.index)
  n = 0
  notebooks = []
  for _, row in df.iterrows():
    driver.get(row['process_url'])
    time.sleep(1)
    notebooks_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for notebook_element in notebooks_elements:
      notebook = {
        'name': notebook_element.find_element_by_xpath('.//h3/a').text,
        'process': row['name'],
        'score': row['score'],
        'price': notebook_element.find_element_by_xpath('.//div[3]/div/a').text,
        'ram': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[2]').text,
        'screen': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[3]').text,
        't video': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[5]/ul').text,
        'storage': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[4]/ul').text,
        'link': notebook_element.find_element_by_xpath('.//h3/a').get_attribute('href'),
      }
      notebooks.append(notebook)
    n = n+1
    print(f'{ round(n*100.0/n_processes, 2)  } % ')

  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de notebooks
  df_notebooks = pd.DataFrame(notebooks)
  df_notebooks.to_csv(time.strftime("%d%m%y_notebooks.csv", time.localtime()))