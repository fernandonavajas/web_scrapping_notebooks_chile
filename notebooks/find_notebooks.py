import pandas as pd
from order_date_prices import order_date_prices
from selenium.webdriver.common.by import By


def find_notebooks(driver):
  print("Searching Notebooks")
  df = pd.read_csv('notebooks/processes.csv')
  n_processes = len(df.index)
  n = 0
  notebooks = []
  for _, row in df.iterrows():
    driver.get(row['process_url'])
    notebooks_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for notebook_element in notebooks_elements:
      notebook = {
        'id': int(notebook_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'notebook': notebook_element.find_element(By.XPATH,'.//h3/a').text,
        'name': row['name'],
        'score': int(row['score']),
        'price': int(notebook_element.find_element(By.XPATH,'.//div[3]/div/a').text.replace("$","").replace(" ","").replace(".","")),
        'ram': notebook_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'screen': notebook_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'graphic card': notebook_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]/ul').text,
        'hard drive': notebook_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]/ul').text,
        'link': notebook_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
      }
      notebooks.append(notebook)
    n = n+1
    print(f'{ round(n*100.0/n_processes, 2)  } % ')
  print("")
  # Guardar la lista de notebooks
  order_date_prices(notebooks, path='items/notebooks.csv', order='score', order_ascending=False)
