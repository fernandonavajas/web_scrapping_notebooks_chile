from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_smartphones(driver):
  print("Searching smartphones")
  smartphones = []
  for index in range(1, 99):
    # Obtener los telefonos
    driver.get('https://www.solotodo.cl/cells?brands=149039&brands=149047&brands=544167&brands=149136&brands=856729&brands=1017974&brands=149235&brands=149242&internal_storage_start=150139&battery_mah_start=3000&ram_start=150264&ordering=offer_price_usd&page='+str(index)+'&')
    smartphones_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not smartphones_elements:
      break
    for smartphone_element in smartphones_elements:
      try:
        smartphone = {
          'id': int(smartphone_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
          'name': smartphone_element.find_element(By.XPATH,'.//h3/a').text,
          'processor': smartphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
          'screen': smartphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
          'capacity': smartphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
          'cam': smartphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
          'so': smartphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
          'url': smartphone_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
          'price': int(smartphone_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
        }
        smartphones.append(smartphone)
      except NoSuchElementException as e:
        print(f'Error en uno de los elementos, e= {e.msg}')
        continue
    
    # Cambiar la pagina
    print(f'{str(index)}')
  
  print(("-"*60).center(100))
  # Guardar la lista de telefonos
  order_date_prices(smartphones, path='items/smartphones.csv')

