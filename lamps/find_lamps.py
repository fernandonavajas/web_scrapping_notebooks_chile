from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_lamps(driver):
  print("Searching lamps")
  lamps = []
  for index in range(1, 99):
    # Obtener las ampolletas
    driver.get('https://www.solotodo.cl/lamps?ordering=offer_price_usd&page='+str(index)+'&')
    lamps_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not lamps_elements:
      break
    for lamp_element in lamps_elements:
      try:
        lamp = {
          'id': int(lamp_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
          'name': lamp_element.find_element(By.XPATH,'.//h3/a').text,
          'socket': lamp_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
          'brightness': lamp_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
          'eq power': lamp_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
          'watts': lamp_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
          'url': lamp_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
          'price': int(lamp_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
        }
        lamps.append(lamp)
      except NoSuchElementException as e:
        print(f'Error en uno de los elementos, e= {e.msg}')
        continue

    # Cambiar la pagina
    print(f'{str(index)}')
  
  print(("-"*60).center(100))
  # Guardar la lista de ampolletas
  order_date_prices(lamps, path='items/lamps.csv')

