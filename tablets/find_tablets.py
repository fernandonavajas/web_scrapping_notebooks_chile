from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices
from selenium.common.exceptions import NoSuchElementException

def find_tablets(driver):
  print("Searching tablets")
  tablets = []
  for index in range(1, 99):
    # Obtener las tablets
    driver.get('https://www.solotodo.cl/tablets?brands=286729&brands=286742&brands=286873&brands=838616&brands=286991&ordering=offer_price_usd&page='+str(index)+'&')
    tablets_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not tablets_elements:
      break
    for tablet_element in tablets_elements:
      try:
        tablet = {
          'id': int(tablet_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
          'name': tablet_element.find_element(By.XPATH,'.//h3/a').text,
          'processor': tablet_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
          'screen': tablet_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
          'capacity': tablet_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
          'phone connet': tablet_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
          'so': tablet_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
          'url': tablet_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
          'price': int(tablet_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
        }
        tablets.append(tablet)
      except NoSuchElementException as e:
        print(f'Error en uno de los elementos, e= {e.msg}')
        continue
  
    #Cambiar la pagina
    print(f'{str(index)}')
  
  print("")
  # Guardar la lista de tablets
  order_date_prices(tablets, path='items/tablets.csv')

