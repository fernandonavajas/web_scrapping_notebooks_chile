import pandas as pd
from order_date_prices import order_date_prices

def find_notebooks(driver):
  df = pd.read_csv('processes.csv')
  n_processes = len(df.index)
  n = 0
  notebooks = []
  for _, row in df.iterrows():
    driver.get(row['process_url'])
    notebooks_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for notebook_element in notebooks_elements:
      notebook = {
        'id': int(notebook_element.find_element_by_xpath('.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'notebook': notebook_element.find_element_by_xpath('.//h3/a').text,
        'name': row['name'],
        'score': int(row['score']),
        'price': int(notebook_element.find_element_by_xpath('.//div[3]/div/a').text.replace("$","").replace(" ","").replace(".","")),
        'ram': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[2]').text,
        'screen': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[3]').text,
        'graphic card': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[5]/ul').text,
        'hard drive': notebook_element.find_element_by_xpath('.//div[2]/dl/dd[4]/ul').text,
        'link': notebook_element.find_element_by_xpath('.//h3/a').get_attribute('href'),
      }
      notebooks.append(notebook)
    n = n+1
    print(f'{ round(n*100.0/n_processes, 2)  } % ')

  # Cerrar el navegador falso
  driver.quit()

  # Guardar la lista de notebooks
  order_date_prices(notebooks)