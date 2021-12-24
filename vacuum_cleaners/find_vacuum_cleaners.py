from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

from order_date_prices import order_date_prices

def find_vacuum_cleaners(driver):
  print("Searching vacuum_cleaners")
  vacuum_cleaners = []
  for index in range(1, 99):
    # Obtener las aspiradoras
    driver.get('https://www.solotodo.cl/vacuum_cleaners?v_types=355633&ordering=offer_price_usd&page='+str(index)+'&')
    vacuum_cleaners_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not vacuum_cleaners_elements:
      break
    for vacuum_cleaner_element in vacuum_cleaners_elements:
      vacuum_cleaner = {
        'id': int(vacuum_cleaner_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': vacuum_cleaner_element.find_element(By.XPATH,'.//h3/a').text,
        'type': vacuum_cleaner_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'power': vacuum_cleaner_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'capacity': vacuum_cleaner_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'storage': vacuum_cleaner_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'url': vacuum_cleaner_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(vacuum_cleaner_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      vacuum_cleaners.append(vacuum_cleaner)
    # Cambiar la pagina
    print(f'{str(index)}')
  print(("-"*60).center(100))
  # Guardar la lista de aspiradoras
  order_date_prices(vacuum_cleaners, path='items/vacuum_cleaners.csv')

