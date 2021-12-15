from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_consoles(driver):
  print("Searching consoles")
  consoles = []
  for index in range(1, 99):
    # Obtener las consolas
    driver.get('https://www.solotodo.cl/consoles?ordering=offer_price_usd&page='+str(index)+'&')
    consoles_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not consoles_elements:
      break
    for console_element in consoles_elements:
      try:
        console = {
          'id': int(console_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
          'name': console_element.find_element(By.XPATH,'.//h3/a').text,
          'model': console_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
          'capacity': console_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
          'format': console_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
          'bundle': console_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
          'url': console_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
          'price': int(console_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
        }
        consoles.append(console)
      except NoSuchElementException as e:
        print(f'Error en uno de los elementos, e= {e.msg}')
        continue

    # Cambiar la pagina
    print(f'{str(index)}')
  
  print("")
  # Guardar la lista de consolas
  order_date_prices(consoles, path='items/consoles.csv')

