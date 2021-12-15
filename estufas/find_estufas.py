from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

from order_date_prices import order_date_prices

def find_estufas(driver):
  print("Searching estufas")
  estufas = []
  for index in range(1, 99):
    # Obtener las estufas
    driver.get('https://www.solotodo.cl/estufas?sh_types=658945&ordering=offer_price_usd&page='+str(index)+'&')
    estufas_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not estufas_elements:
      break
    for estufa_element in estufas_elements:
      estufa = {
        'id': int(estufa_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': estufa_element.find_element(By.XPATH,'.//h3/a').text,
        'type': estufa_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'watts': estufa_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'm2': estufa_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'm3': estufa_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'url': estufa_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(estufa_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      estufas.append(estufa)
    # Cambiar la pagina
    print(f'{str(index)}')
  print("")
  # Guardar la lista de estufas
  order_date_prices(estufas, path='items/estufas.csv')

